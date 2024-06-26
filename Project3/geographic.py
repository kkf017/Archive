import math
import geopy

from typing import Tuple, Union

#https://www.boites-a-livres.fr/

# pip install geopy
# pip install googlesearch-python

LANGUAGE = "eng"

class Location:
	""" Class containing informations about a location. """
	def __init__(self, addr:str, latitud:float, longitud:float)->None:
		self.addr = addr
		self.latitud = latitud
		self.longitud = longitud
		
		self.x, self.y, self.z = self.CoordSphere(self.latitud, self.longitud)
	
	def CoordSphere(self, delta:float, phi:float)->Tuple[float]:
		""" Function to compute spherical coordinates of a point. """
		R = 6371
		radian = lambda degree: degree * math.pi / 180
		
		delta, phi = (radian(delta), radian(phi))
				
		x = R * math.cos(delta) * math.cos(phi)
		y = R * math.cos(delta) * math.sin(phi)
		z = R *  math.sin(delta)
		return (x, y, z)
		

def coordinates(location:str)->Tuple[Union[str, float]]:
	""" Function to get coordinates of a location. """	
	coder = geopy.geocoders.Nominatim(user_agent="GetLoc")
	loc = coder.geocode(location, language=LANGUAGE)
	if loc == None:
		return (None, None, None)
	return (loc.address, loc.latitude, loc.longitude)
		

def euclidean(x:Tuple[float], y:Tuple[float])->float:
	""" Function to compute ...(km) between two points. """
	x1, y1, z1 = x
	x2, y2, z2 = y
	return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
	
	
if __name__ == "__main__":
	
	addr1 = "36 rue de la Prairie Saint Genis-Pouilly"
	addr2 = "162 Rue du Vieux Bourg, Ségny"
	
	addr, latitude, longitude = coordinates(addr1)
	loc1 = Location(addr, latitude, longitude)
	print(f"\n{loc1.addr}")
	print(f"Latitude={loc1.latitud}")
	print(f"Longitude={loc1.longitud}")
	
	
	addr, latitude, longitude = coordinates(addr2)
	loc2 = Location(addr, latitude, longitude)
	print(f"\n{loc2.addr}")
	print(f"Latitude={loc2.latitud}")
	print(f"Longitude={loc2.longitud}")

	x = euclidean((loc1.x, loc1.y, loc1.z), (loc2.x, loc2.y, loc2.z))
	print(f"\nEuclidean: {x}")
	
