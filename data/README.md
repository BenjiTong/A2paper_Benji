# deploy the data processing lambda function

```shell

make deploy

```

Pls ensure your aws have the right configure.

# trigger the crawler

Open the lambda page to find the start_crawler function. Following the page sending a test msg with any content. The whole processing will be started.

http://blog.sciencenet.cn/blog-3247241-1249807.html
Suomi NPP VIIRS夜间灯光遥感数据简介与下载（一）——数据介绍，FTP下载与hdf5读取


http://blog.sina.com.cn/s/blog_764b1e9d0102zzvk.html#cmt_5F0C3F16-B7EC438A-17C53590C-83A-8D3
夜光遥感数据处理 此博文包含图片 (2020-07-10 15:11:25)

https://blog.csdn.net/weixin_41666747/article/details/100571533
Python读取夜间灯光数据看中国城市发展


https://leafmap.org/notebooks/03_cog_stac/
Using Cloud Optimized GeoTIFF (COG) and SpatioTemporal Asset Catalog (STAC)

NPP-VIIRS DNB daily data in natural disaster assessment: Evidence from selected case studies

-i https://pypi.tuna.tsinghua.edu.cn/simple


https://github.com/tsooryakie/skyglow-fft


https://stacindex.org/ecosystem?category=API


http://www.fao.org/home/en/   全球区域划分 https://data.apps.fao.org/map/catalog/srv/api/records/9c35ba10-5649-41c8-bdfc-eb78e9e65654

http://www.naturalearthdata.com/downloads/10m-cultural-vectors/

https://nordpil.com/resources/world-database-of-large-cities/


git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch data/GDNBO_npp_d20210617_t1922462_e1928266_b49946_c20210617232827917011_oeac_ops.li.co.tif" --prune-empty --tag-name-filter cat -- --all

git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch data/SVDNB_npp_d20210617_t1922462_e1928266_b49946_c20210617232827927575_oeac_ops.rade9.co.tif" --prune-empty --tag-name-filter cat -- --all

git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch data/SVM15_npp_d20210610_t1446587_e1452391_b49844_c20210610185240200675_oeac_ops.rad.co.tif" --prune-empty --tag-name-filter cat -- --all

git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch projects/Moon.mp3' --prune-empty --tag-name-filter cat -- --all

https://gdal.org/tutorials/raster_api_tut.html

https://stacspec.org/

https://www.linkedin.com/pulse/how-sunny-my-city-better-process-stac-sentinel2-lambda-alvaro-huarte