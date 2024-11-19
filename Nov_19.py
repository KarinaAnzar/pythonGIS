import geopandas as gpd
import fiona
import matplotlib.pyplot as plt

gdb_path = r"\\itnas.memphis.edu\uomhome$\kanzar\My Documents\GIS\geoportal.gdb\geoportal.gdb"

def explore_gdb(gdb_path):
    layers = fiona.listlayers(gdb_path)
    for layer in layers:
        print(f'Layer name:{layer}')
        gdf = gpd.read_file(gdb_path, layer=layer)
        print(f'EPSG code : {gdf.crs}')
        print(f'Number of rows is : {len(gdf)}')
        print(f'geometry type is: {gdf.geom_type.unique()}')
        print(f'columns are : {list(gdf.columns)}\n')
        fig, ax = plt.subplots(figsize=(8, 6))
        gdf.plot(ax=ax)
        ax.set_title(f'Layer : {layer}')
        plt.show()

explore_gdb(gdb_path)