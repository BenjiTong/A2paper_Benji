import json
from urllib.request import urlopen

ChinaArea = [108.990515,20.319485,130.478558,40.992357]
NZArea = [163.888049,-31.69433,-171.825824,-52.621956]
MiddleEastArea = [35.991737,39.298213,72.78633,24.828731]

MAX_ITEM = 100
MAX_LINK = 5
global counter
counter = 0

# [108.990515,20.319485,            130.478558,40.992357]
# [-5.00208333335, 61.00208322135,  119.99791766665, 75.00208333335]
def is_overlap(bbox1, bbox2):
    x1 = max(bbox1[0],bbox2[0]) #108
    y1 = max(bbox1[1],bbox2[1]) #130 
    x2 = min(bbox1[2],bbox2[2]) #119
    y2 = min(bbox1[3],bbox2[3]) #40
    if x1 < x2 and y1 < y2:
        return True
    else:
        return False

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

def deal_with_tif_info(json):
    global counter
    print(json['properties']['datetime'])
    if is_overlap(ChinaArea, json['bbox']):
        counter += 1
        print(json['assets']['image']['href'])
        print(json['bbox'])
        # push tif to SNS

# STAC processing...  sqs: child-link and push item into sns
def native_handle_sqs(url = 'https://globalnightlight.s3.amazonaws.com/VIIRS_npp_catalog.json'):
    global counter
    if counter >= MAX_ITEM:
        print('reach peak counter:' + str(counter) +' from sns: ' + url)
        return
    print('from sqs: ' + url)
    catalog = url_to_json(url)
    child_links, items = get_links(catalog, url)
    for index, clink in enumerate(child_links):
        if index >= MAX_LINK:
            break
        print('into native handle:' + str(index) + " url:" + url)
        native_handle_sqs(clink)  # can be pushed to SQS
    for item in items:
        if counter >= MAX_ITEM:
            print('reach peak counter:' + str(counter))
            break
        deal_with_tif_info(url_to_json(item)) 

native_handle_sqs() # trigger start

