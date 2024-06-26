import csv

from database import *
		

def populate(filename:str, name:str):
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			insert(name, (row[0], float(row[1]), float(row[2])))				

if __name__ == "__main__":
	
	table = "Location"
	create(table, "Address, Latitud, Longitud")
	populate("Ain.csv", table)
	#populate("Haute-Savoie.csv", table)
	print("\n\n\n********************************************")
	select(table, f"SELECT * FROM {table}")
	
