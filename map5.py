import folium
import os
import json
from folium import plugins

my_map = folium.Map(location=[18.490134, 74.025581], zoom_start=17)
style1 = {'fillColor': '#228822', 'color': '#000000'}
lay = os.path.join("layer1.geojson")
folium.GeoJson(lay, name='building', style_function=lambda x: style1).add_to(my_map)
plugins.Geocoder().add_to(my_map)
plugins.MeasureControl().add_to(my_map)

folium.Marker(location=[18.4937, 74.0189]).add_to(my_map)
paths = 'paths/soe.geojson'


def switchPosition(coordinate):
    temp = coordinate[0]
    coordinate[0] = coordinate[1]
    coordinate[1] = temp
    return coordinate

with open(paths) as f:
    test = json.load(f)


for feature in test["features"]:
    path = feature['geometry']['coordinates']
    final_path = list(map(switchPosition, path))
    print(final_path)

# Add an AntPath to the map
plugins.AntPath(locations=final_path).add_to(my_map)
my_map.save("my_map.html")
my_map
