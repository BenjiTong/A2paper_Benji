import json
import os
from os import wait
from urllib.request import urlopen
import boto3
import numpy as np
from osgeo import gdal
from file_utils import FileUtils
from osgeo_utils import OgrCommonUtils, GdalCommonUtils
from sm_mysql import Sec_Mysql
import datetime 

wait_area = FileUtils.WAIT_LIST
native_run = FileUtils.native_run

s3 = boto3.client('s3')

def lambda_handler(event, context):
    records = event['Records']
    to_be_visited_queue = os.environ['CATALOG_CRAWL_QUEUE']
    item_topic_arn = os.environ['STAC_ITEM_TOPIC']
    max_link = int(os.environ['MAX_CHILDREN'])
    max_item = int(os.environ['MAX_ITEM'])
    for record in records:
        r = json.loads(record['body'])
        process(r['url'], r['bbox'], r['datetime'], r['city_id'])

def process(item_path, bbox, date_time, city_id):   
    area = wait_area[city_id]
    # # download file
    # bucket_name, prefix_path, file_name = FileUtils.parse_s3_path(item_path)
    
    # file_name = '/tmp/{}'.format(file_name)
    conn = Sec_Mysql.get_mysql_conn()

    file_name = '/vsicurl/{}'.format(item_path)
    
    try:
        cur = conn.cursor()
        cur.execute("select id from main where city_id='{}' and file='{}'".format(city_id, file_name))
        cur.fetchall()
        conn.commit()  
        cnt = cur.rowcount   
        cur.close()   
        if cnt > 0:
            print('[INFO]Duplicate! file is {}, city is {}'.format(file_name, city_id))
            return
    except Exception as e:
        conn.rollback()
        conn.close()
        print("[ERROR]Database connection failed or excute error due to {}".format(e)) 
        return
    
    #.replace('s3://','/vsis3/')

    # if FileUtils.exist_s3_path(s3, item_path) and not FileUtils.exsit_native_path(file_name):
    #     print(bucket_name+": " + prefix_path + ": "+ file_name)
    #     s3.download_file(bucket_name, prefix_path, file_name)
    # calculate intersects
    wait_geometry = OgrCommonUtils.create_geometry_from_bbox(area[0],area[1],area[2],area[3])
    try:
        s3_dataset = gdal.Open(file_name, gdal.GA_ReadOnly)
    except Exception as e:
        print('[ERROR] GDAL get file error {}'.format(e))
        return
    s3_extent = GdalCommonUtils.get_envelope(s3_dataset)
    s3_geometry = OgrCommonUtils.create_geometry_from_bbox(s3_extent[0],s3_extent[1],s3_extent[2],s3_extent[3])
    if not wait_geometry.Intersects(s3_geometry):
        print('[INFO]do not intersect,exit! file is '+ file_name)
        return
    
    aoi_geometry = s3_geometry.Intersection(wait_geometry)

    temp_x_min, temp_x_max, temp_y_min, temp_y_max = aoi_geometry.GetEnvelope()
    aoi_x_min = max(temp_x_min, area[0])
    aoi_y_min = max(temp_y_min, area[1])
    aoi_x_max = min(temp_x_max, area[2])
    aoi_y_max = min(temp_y_max, area[3])
    aoi_extent = [aoi_x_min, aoi_y_min, aoi_x_max, aoi_y_max]
    print('[INFO]IOU Envelope={}'.format(aoi_extent))

    # Get raster data from input Datasets.
    left, top, right, bottom = GdalCommonUtils.get_reading_window(s3_dataset, aoi_extent)
    print('[INFO]s3 Dataset Window=({},{},{},{}) Size=({},{})'.format(left, top, right, bottom, right-left, bottom-top))
    s3_raster = s3_dataset.GetRasterBand(1).ReadAsArray(xoff=left, yoff=top, win_xsize=right-left, win_ysize=bottom-top)


    # Calculate final results and save data.
    valid_mask = (s3_raster != -999.3)
    s3_raster[~valid_mask] = 0
    valid_mask = (s3_raster != -1.5)
    s3_raster[~valid_mask] = 0
    valid_mask = (s3_raster > 0.3)
    s3_raster[~valid_mask] = 0
    
    count_of_value_pixels = np.count_nonzero(s3_raster > 0.3)
    sum_of_value_pixels = np.sum(s3_raster)

    if count_of_value_pixels == 0:
        print('[INFO]filter zero area: {}'.format(file_name))
        return

    del s3_raster
    # FileUtils.delete_native_file(file_name)


    sql = ("INSERT INTO main(`datetime`, `radiance`, `pixels`, `city_id`, `window`, `file`) VALUES (%s, %s, %s, %s, %s, %s)")
    data = (date_time, str(sum_of_value_pixels), count_of_value_pixels, city_id, str(bbox), file_name)
    print("INSERT INTO main(`datetime`, `radiance`, `pixels`, `city_id`, `window`, `file`) VALUES ({}, {}, {}, {}, {}, {})".format(date_time, str(sum_of_value_pixels), count_of_value_pixels, city_id, str(bbox), file_name))
    try:
        cur = conn.cursor()
        cur.execute(sql,data)
        conn.commit()
        cur.close()
        conn.close()
        print('[INFO]{} insert success!'.format(file_name))
    except Exception as e:
        conn.rollback()
        conn.close()
        print("[ERROR]Database connection failed or excute error due to {}".format(e))  
        
    return '[INFO]process over:{}'.format(file_name)

# process('https://globalnightlight.s3.amazonaws.com/201305/SVDNB_npp_d20130501_t1856278_e1902082_b07823_c20130502010209874894_noaa_ops.rade9.co.tif',
# [
#         124.997916665,
#         36.002061735,
#         177.997959065,
#         63.002083335
#     ],"2012-05-01T16:09:06Z",0
# )

