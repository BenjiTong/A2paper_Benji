import libtiff
import matplotlib.pyplot as plt

exit()
tif = TIFF.open('npp_d20210630_t2355596_e0001399_b50133.vflag.co.tif',mode='r')
img = tif.read_image()

lons = 100; lone = 137; lats = 15; late = 52

lons_grid = int((lons+180.0)/(30.0/3600))
lone_grid = int((lone+180.0)/(30.0/3600))

lats_grid = int((75.0 - lats)/(30.0/3600))
late_grid = int((75.0 - late)/(30.0/3600))

img2 = img[late_grid:lats_grid,lons_grid:lone_grid]

plt.imshow(img2)
plt.show()
