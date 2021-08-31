import os
import json
import boto3
from urllib.request import urlopen
from file_utils import FileUtils

SQS_CLIENT = boto3.client('sqs') 

global url 
url = 'https://globalnightlight.s3.amazonaws.com/VIIRS_npp_catalog.json'

wait_area = FileUtils.WAIT_LIST
 
global counter
counter = 0



def url_to_json(url: str):
    with urlopen(url) as furl:
        content = furl.read()
    return json.loads(content)

def get_links(catalog: json, url: str):
    children = list()
    items = list()
    base_url = ''
    if not catalog['links'][0]['href'].startswith('http'):
        part = url.rpartition('/')
        base_url = part[0] + part[1]
    for link in catalog['links']:
        if link['rel'] == 'child':
            children.append(base_url + ((link['href']).replace('./','')))
        if link['rel'] == 'item':
            items.append(base_url + ((link['href']).replace('./','')))
    return children, items

 

# STAC processing...  sqs: child-link and push item into sns
def native_handle_sqs(event, context):
    global counter
    records = event['Records']
    to_be_visited_queue = os.environ['CATALOG_CRAWL_QUEUE']
    item_topic_arn = os.environ['STAC_ITEM_TOPIC']
    max_link = int(os.environ['MAX_CHILDREN'])
    max_item = int(os.environ['MAX_ITEM'])

    for record in records:    
        url = record['body']
        if counter >= max_item:
            print('reach peak counter:' + str(counter) +' from sns: ' + url)
            return
        
        catalog = url_to_json(url)
        child_links, items = get_links(catalog, url)
        for index, clink in enumerate(child_links):
            if index >= max_link:
                break
            SQS_CLIENT.send_message(QueueUrl=to_be_visited_queue,
                                        MessageBody=clink)
            print('Catalog inserted: ', clink)
            #native_handle_sqs(clink)  # can be pushed to SQS

        for item in items:
            if counter >= max_item:
                print('reach peak counter:' + str(counter))
                break
            itr = url_to_json(item)
            for idx, area in wait_area.items():
                if FileUtils.is_overlap(area, itr['bbox']):
                    counter += 1
                    result = {
                        'city_id': idx,
                        'bbox': itr['bbox'],
                        'url': itr['assets']['image']['href'],
                        # .replace('https://globalnightlight.s3.amazonaws.com','s://globalnightlight'),
                        'datetime': itr['properties']['datetime']
                    }
                    SQS_CLIENT.send_message(QueueUrl=item_topic_arn,
                                            MessageBody=json.dumps(result))
                    # push tif to SNS*

def sqs_handler(event, context):
    native_handle_sqs(event, context)


def start_handler(event, context):
    SQS_CLIENT.send_message(QueueUrl=os.environ['CATALOG_CRAWL_QUEUE'],
                            MessageBody=url)
    print('Inserting root catalog', url)