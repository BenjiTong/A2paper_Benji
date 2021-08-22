from ukis_pysat.data import Source
from ukis_pysat.file import get_sentinel_scene_from_dir
from ukis_pysat.members import Datahub, Platform
from ukis_pysat.raster import Image

# connect to Copernicus Open Access Hub  and query metadata
src = Source(Datahub.Scihub)
meta = src.query_metadata(
    platform=Platform.Sentinel2,
    date=("20200101", "NOW"),
    aoi=(11.90, 51.46, 11.94, 51.50),
    cloud_cover=(0, 50),
)
for item in meta:  # item is now a PySTAC item
    print(item.id)
    uuid = item.properties["srcuuid"]

    # download geocoded quicklook and image
    src.download_quicklook(product_uuid=uuid, target_dir="tmp")
    src.download_image(product_uuid=uuid, target_dir="tmp")

    break

# get sentinel scene from directory
with get_sentinel_scene_from_dir("tmp") as (full_path, ident):
    with Image(full_path.join("pre_nrcs.tif")) as img:
        # scale the image array, having one band
        img.arr = img.arr * 0.3