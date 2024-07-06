import folium


latlon = [(46.2838474, 6.0858372), (46.2764726, 6.0943786), (46.27169189999999, 6.095952650374953), (46.2706077, 6.100693), (46.26696, 6.097865), (46.2647609, 6.095296532772116), (46.296085, 6.072697)]
mapit = folium.Map( location=(46.263996,6.029845731313132), zoom_start=6 ) #None
for coord in latlon:
    folium.Marker( location=[ coord[0], coord[1] ], fill_color='#43d9de', radius=8 ).add_to( mapit )
   
    

    
mapit.save('map.html')
