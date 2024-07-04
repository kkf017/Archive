import csv
import math

from services.database import *
from services.geography import Location, coordinates, euclidean	

from typing import List, Dict, Union


# Revoir database :
	#(Hash, address, commune, department, region, code postal, pays, latitude, longitude)
			# ORDER BY ...

def fill()->List[str]:
	request = f"SELECT * FROM {TABLE}" # order by alphabetical order
	
	result = []
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	rows = cursor.execute(request)
	for row in rows:
		result.append(row[0])
	db.commit()
	db.close()
	return result

def sphere(location:str, radius:float)->Dict[str, List[Dict[str, Union[str, float]]]]:
	addr, latitud, longitud = coordinates(location)
	if (addr == None and latitud == None and longitud == None):
		return []
	loc1 = Location(addr, latitud, longitud)
	
	const = loc1.nearest(radius)
	rad = math.pi / 180
	request = f"SELECT * FROM {TABLE} a WHERE ( {const} <= {loc1.x} * cos(a.latitud * {rad}) * cos(a.longitud * {rad}) + {loc1.y} * cos(a.latitud * {rad}) * sin(a.longitud * {rad}) + {loc1.z} * sin(a.latitud * {rad})  )"
	
	result = []
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	rows = cursor.execute(request)
	for row in rows:
		new = {}
		loc2 = Location(row[0], float(row[1]), float(row[2]))
		new["Address"] = row[0]
		new["distance"] = '{:.2f}'.format(euclidean(loc1,loc2))
		result.append(new)
	db.commit()
	db.close()
	
	solution = {}
	solution["Location"] = loc1.addr
	solution["result"] = result
	return solution
			
	
	
