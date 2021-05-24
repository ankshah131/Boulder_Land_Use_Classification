import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon


def bbox(min_long, min_lat, max_long, max_lat):                                                                                                                  
    return Polygon([[min_long, min_lat],[min_long, max_lat],
    [max_long,max_lat],[max_long,min_lat]])

gpd.GeoDataFrame(pd.DataFrame(['p1'], columns = ['geom']),
     crs = {'init':'epsg:4326'},
     geometry = [bbox(-105.28590, 40.00636, -105.21664, 40.05062)]).to_file('AOI.shp')