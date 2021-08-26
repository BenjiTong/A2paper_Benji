import json
import os
from os import wait
from urllib.request import urlopen
import boto3
import numpy as np
from osgeo import gdal
from file_utils import FileUtils
from osgeo_utils import OgrCommonUtils, GdalCommonUtils

NATIVE = True
ChinaArea = [108.990515,20.319485,130.478558,40.992357]

item_path = 's3://globalnightlight/201204/SVDNB_npp_d20120401_t1901195_e1906599_b02219_c20120402010701174040_noaa_ops.rade9.co.tif'
bbox = [81.997916665, 13.002063335000003, 118.997946265, 38.002083335]

s3 = boto3.client('s3')

def lambda_handler(event, context):
    records = event['Records']
    to_be_visited_queue = os.environ['CATALOG_CRAWL_QUEUE']
    item_topic_arn = os.environ['STAC_ITEM_TOPIC']
    max_link = int(os.environ['MAX_CHILDREN'])
    max_item = int(os.environ['MAX_ITEM'])
    for record in records:
        process()

def process():   
    # download file
    bucket_name, prefix_path, file_name = FileUtils.parse_s3_path(item_path)
    if FileUtils.exist_s3_path(s3, item_path) and not FileUtils.exsit_native_path(file_name):
        print(bucket_name+": " + prefix_path + ": "+ file_name)
        s3.download_file(bucket_name, prefix_path, file_name)
    # calculate intersects
    wait_geometry = OgrCommonUtils.create_geometry_from_bbox(ChinaArea[0],ChinaArea[1],ChinaArea[2],ChinaArea[3])
    s3_dataset = gdal.Open(file_name, gdal.GA_ReadOnly)
    s3_extent = GdalCommonUtils.get_envelope(s3_dataset)
    s3_geometry = OgrCommonUtils.create_geometry_from_bbox(s3_extent[0],s3_extent[1],s3_extent[2],s3_extent[3])
    if not wait_geometry.Intersects(s3_geometry):
        print('INFO:do not intersect,exit! file is '+ file_name)
        return {
            'statusCode': 200,
            'body': json.dumps('Input data do not intersect! file is '+ file_name)
        }
    
    aoi_geometry = s3_geometry.Intersection(wait_geometry)

    temp_x_min, temp_x_max, temp_y_min, temp_y_max = aoi_geometry.GetEnvelope()
    aoi_x_min = max(temp_x_min, ChinaArea[0])
    aoi_y_min = max(temp_y_min, ChinaArea[1])
    aoi_x_max = min(temp_x_max, ChinaArea[2])
    aoi_y_max = min(temp_y_max, ChinaArea[3])
    aoi_extent = [aoi_x_min, aoi_y_min, aoi_x_max, aoi_y_max]
    print('INFO: IOU Envelope={}'.format(aoi_extent))

    # Get raster data from input Datasets.
    left, top, right, bottom = GdalCommonUtils.get_reading_window(s3_dataset, aoi_extent)
    print(' + s3 Dataset Window=({},{},{},{}) Size=({},{})'.format(left, top, right, bottom, right-left, bottom-top))
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

    avg_radiance = sum_of_value_pixels / count_of_value_pixels
    print('avg_radience:' + str(avg_radiance))

