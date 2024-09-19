import folium
import os
import csv

def display():
    global my_map
    my_map = folium.Map(location=[18.490134, 74.025581], zoom_start=17)
    style1 = {'fillColor': '#228822', 'color': '#000000'}
    lay = os.path.join('layer1.geojson')
    folium.GeoJson(lay, name='building', style_function=lambda x: style1).add_to(my_map)
    
    # Add a marker at the location
    folium.Marker([lati, longi], popup=folium.Popup(name, max_width=500)).add_to(my_map)
    my_map.save("my_map.html")

n = input("Enter value: ")

with open('Coor.csv', 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        if n == row[0]:
            print(row)
            name = row[0]
            lati = float(row[1])  
            longi = float(row[2]) 
            display()
            break

my_map
