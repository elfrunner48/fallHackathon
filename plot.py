import descartes
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pds
from shapely.geometry import Point, Polygon
import sqlite3



def main():
    # Get (lat, long) from database
    start_list, final_list = get_data()
    

    # Get map
    map()
    

def get_data():
    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT latitudeStart, longitudeStart FROM locations')
    start_list = cursor.fetchall()
    conn.close()

    conn = sqlite3.connect('locations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT latitudeFinal, longitudeFinal FROM locations')
    final_list = cursor.fetchall()
    conn.close()

    return start_list, final_list
    

def map():
    street_map = gpd.read_file(r"C:\Users\nafla\OneDrive\Documents\Hackathon\kx-memphis-tn-major-roads-SHP\memphis-tn-major-roads.shp")
    fig, ax = plt.subplots(figsize=(15,15))
    street_map.plot(ax=ax)


    plt.show()
   

if __name__ == "__main__":
    main()
