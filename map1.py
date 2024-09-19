import folium
from folium import plugins
my_map folium.Map(location [18.490134, 74.025581), zoom_start=17)
my_map.add_child(folium.LatLngPopup())
folium.plugins.Geocoder().add_to(my_map)
my_map