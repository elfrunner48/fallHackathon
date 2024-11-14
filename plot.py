import descartes
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
import sqlite3


def main():
    # Get (lat, long) from database
    start_list, final_list = get_data()

    # Plot map with vectors
    plot_map_with_vectors(start_list, final_list)


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


def plot_map_with_vectors(start_list, final_list):
    # Load the map shapefile
    street_map = gpd.read_file(r"C:\Users\nafla\OneDrive\Documents\Hackathon\tennessee-latest-free.shp\gis_osm_roads_free_1.shp")
    
    # Plot the street map
    fig, ax = plt.subplots(figsize=(15, 15))
    street_map.plot(ax=ax, color="lightgray")

    # Iterate through start and final location lists to create and plot vectors
    for start, final in zip(start_list, final_list):
        # Create start and final points
        print(start, final)
        if start[0] == None or start[1] == None or final[0] == None or final[1] == None:
            continue
        start_point = Point(start[1], start[0])  # (longitude, latitude)
        final_point = Point(final[1], final[0])  # (longitude, latitude)

        # Create a line (vector) from start to final
        line = LineString([start_point, final_point])

        # Plot the line on the map
        gpd.GeoSeries([line]).plot(ax=ax, color="blue", linewidth=2)

    # Show the map with vectors
    plt.show()


if __name__ == "__main__":
    main()
