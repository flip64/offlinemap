 
import matplotlib.pyplot  as plt
import io
import urllib,base64
import geopandas as gpd
import matplotlib.pyplot as plt
import shapefile
import contextily as ctx


def uri():
    file_path1="map/shipfile/Iran.shp"
    file_path2="map/shipfile/karkheh.shp"
    file_path3="map/shipfile/kdam.shp"
    shapefile1 = gpd.read_file(file_path1)
    shapefile2 = gpd.read_file(file_path2)
    shapefile3 = gpd.read_file(file_path3)
    shapefile1=  shapefile1.to_crs ({'init':"epsg:4326"})
    shapefile2 = shapefile2.to_crs ({'init':"epsg:4326"})
    shapefile3 = shapefile3.to_crs ({'init':"epsg:4326"})
   
    ax=shapefile2.plot()
    #ctx.base_map(ax)
    fig, ax = plt.subplots()
    shapefile1.plot(ax=ax, color='wheat')
    shapefile2.plot(ax=ax, color='blue')
    shapefile3.plot(ax=ax, color='green')
    List=[shapefile1,shapefile2]
    
    plt.legend(['First List', 'Second List'], loc='upper left')
    plt.savefig('static/img/myplot.png',format= 'png' , dpi=800,bbox_inches='tight')
   #plt.show()
    plt.close()
    fig=plt.gcf()
    buf=io.BytesIO()
 #   fig.savefig(buf,format="png",dpi=800)
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    
    return uri
    

