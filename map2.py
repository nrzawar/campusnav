import folium
import os
from folium import plugins

my_map = folium.Map(location=[18.490134, 74.025581], zoom_start=17)
style1 = {'fillColor': '#228822', 'color': '#000000'}
plugins.Geocoder().add_to(my_map)

# Correct the syntax for joining the path to the geojson file
lay = os.path.join('layer1.geojson')

# Correct lambda function syntax for style_function
folium.GeoJson(lay, name='building', style_function=lambda x: style1).add_to(my_map)

folium.LayerControl().add_to(my_map)
my_map
