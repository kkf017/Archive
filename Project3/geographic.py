import math
import geopy

from typing import Tuple, Union

#https://www.boites-a-livres.fr/

# pip install geopy
# pip install googlesearch-python

LANGUAGE = "eng"
R = 6371 # radius of Earth 

class Location:
	""" Class containing informations about a location. """
	def __init__(self, addr:str, latitud:float, longitud:float)->None:
		self.addr = addr
		self.latitud = latitud
		self.longitud = longitud
		
		self.x, self.y, self.z = self.CoordSphere(self.latitud, self.longitud)
	
	def CoordSphere(self, delta:float, phi:float)->Tuple[float]:
		""" Function to compute spherical coordinates of a point. """
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
	
	
	
########################################################################################
import csv

def nearest(x:str, radius:float)->Tuple[float]:
	addr, latitude, longitude = coordinates(x)
	loc1 = Location(addr, latitude, longitude)
	
	const = (R**2 - (radius**2 - (loc1.x**2+loc1.y**2+loc1.z**2))) / (2*R)
	return (loc1.x, loc1.y, loc1.z, const)


# https://stackoverflow.com/questions/7783684/select-coordinates-which-fall-within-a-radius-of-a-central-point

if __name__ == "__main__":
	
	addr1 = "36 rue de la Prairie Saint Genis-Pouilly"
	radius = 10 # radius of 10 km
	
	x1, y1, z1, const = nearest(addr1, radius)

	filename = "Ain/Ain.csv"
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			loc2 = Location(row[0], float(row[1]), float(row[2]))
			print(f"\n\n{row[0]} \n{float(row[1])}, {float(row[2])}")
			
			
			res = x1*math.cos(loc2.latitud* math.pi / 180)*math.cos(loc2.longitud* math.pi / 180) + y1*math.cos(loc2.latitud* math.pi / 180)*math.sin(loc2.longitud* math.pi / 180) + z1*math.sin(loc2.latitud* math.pi / 180)# formula - SQL
	
			dist = euclidean((loc1.x, loc1.y, loc1.z), (loc2.x, loc2.y, loc2.z))
	
			print(f"Euclidean: {dist}, {const} < {res}  {const < res}")
			input()
	
