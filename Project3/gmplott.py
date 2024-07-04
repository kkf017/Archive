from gmplot import gmplot

# Initialize the map at a given point
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)

# Add a marker
gmap.marker(37.770776, -122.461689, 'cornflowerblue')

# Draw map into HTML file
gmap.draw("my_map.html")



import folium
latlon = [ (51.249443914705175, -0.13878830247011467), (51.249443914705175, -0.13878830247011467), (51.249768239976866, -2.8610415615063034)]
mapit = folium.Map( location=[52.667989, -1.464582], zoom_start=6 ) #None
for coord in latlon:
    folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )

mapit.save( 'map.html')
