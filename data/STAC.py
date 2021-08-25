from intake import open_stac_catalog

catalog_url = 'https://globalnightlight.s3.amazonaws.com/201204/SVDNB_npp_d20120401_t0031464_e0037268_b02208_c20120428182646412163_devl_pop.rade9.co.json'
cat = open_stac_catalog(catalog_url)
print('adfadf')
print(cat)
cat['SVDNB_npp_d20120401_t0031464_e0037268_b02208_c20120428182646412163_devl_pop.rade9.co'].metadata
da = cat['SVDNB_npp_d20120401_t0031464_e0037268_b02208_c20120428182646412163_devl_pop.rade9.co']['thumbnail'].to_dask()
da
