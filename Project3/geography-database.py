import csv
import math

from database import *
from geography import Location, euclidean, nearest		

from typing import List, Dict, Union


# Add hash -  to database ->> TABLE: (Hash, Address, latitud, longitud)


def populate(filename:str, name:str)->None:
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			insert(name, (row[0], float(row[1]), float(row[2])))


def sphere(table:str, location:str, radius:float)->List[Dict[str, Union[str, float]]]:
	x1, y1, z1, const = nearest(location, radius)
	rad = math.pi / 180
	request = f"SELECT * FROM {table} a WHERE ( {const} <= {x1} * cos(a.latitud * {rad}) * cos(a.longitud * {rad}) + {y1} * cos(a.latitud * {rad}) * sin(a.longitud * {rad}) + {z1} * sin(a.latitud * {rad})  )"
	
	result = []
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	rows = cursor.execute(request)
	for row in rows:
		new = {}
		location = Location(row[0], float(row[1]), float(row[2]))
		new["Address"] = row[0]
		new["distance"] = euclidean((x1, y1, z1), (location.x, location.y, location.z))
		result.append(new)
	db.commit()
	db.close()
	for res in result:
		x = new["distance"]
		y = new["Address"]
		print(f"\n{y} - {x}")
	return result
				

if __name__ == "__main__":
	
	table = "Location"
	
	drop(table)
	create(table, "Address, Latitud, Longitud")
	
	populate("Ain/Ain.csv", table)
	#populate("Haute-Savoie/Haute-Savoie.csv", table)
	
	print("\n\n\n********************************************")
	
	#select(table, f"SELECT * FROM {table}")
	sphere(table, "36 rue de la Prairie Saint Genis-Pouilly", 10)
	
