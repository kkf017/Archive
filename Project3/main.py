import csv
import math

from database import *
from geographic import nearest		


def populate(filename:str, name:str):
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			insert(name, (row[0], float(row[1]), float(row[2])))

def sphere(table:str, location:str, radius:float):
	x1, y1, z1, const = nearest(location, radius)
	rad = math.pi / 180
	request = f"SELECT * FROM {table} a WHERE ( {const} <= {x1} * cos(a.latitud * {rad}) * cos(a.longitud * {rad}) + {y1} * cos(a.latitud * {rad}) * sin(a.longitud * {rad}) + {z1} * sin(a.latitud * {rad})  )"
	select(table, request)
				

if __name__ == "__main__":
	
	table = "Location"
	create(table, "Address, Latitud, Longitud")
	
	populate("Ain/Ain.csv", table)
	#populate("Haute-Savoie/Haute-Savoie.csv", table)
	
	print("\n\n\n********************************************")
	
	#select(table, f"SELECT * FROM {table}")
	sphere(table, "36 rue de la Prairie Saint Genis-Pouilly", 10)
	
