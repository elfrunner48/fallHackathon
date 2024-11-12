import descartes
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pds
from shapely.geometry import Point, Polygon
import sqlite3



def main():
    # Get (lat, long) from database
    locations = get_lat_long()

    # Get map
    map()
    



def get_lat_long():
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT latitude, longitude FROM locations')
    data = cursor.fetchall()
    conn.close()
    return data

def map():
    street_map = gpd.read_file(r"C:\Users\nafla\OneDrive\Documents\Hackathon\kx-memphis-tn-major-roads-SHP\memphis-tn-major-roads.shp")
    fig, ax = plt.subplots(figsize=(15,15))
    street_map.plot(ax=ax)

    plt.show()
   

if __name__ == "__main__":
    main()
