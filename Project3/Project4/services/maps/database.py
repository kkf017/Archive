import os.path
import csv
import sqlite3

from services.config import PATH

from typing import Tuple, Optional, Any


DATABASE = os.path.join(PATH, 'geographic.db')
TABLE = "Location"

def drop(table:str)->sqlite3.Cursor:
	return request(f"DROP TABLE IF EXISTS {table};", False)
	

def create(table:str, columns:str)->sqlite3.Cursor:
	drop(table)
	return request(f"CREATE TABLE {table} ({columns})", False)
	
	
def insert(table:str, values:Tuple[Any])->sqlite3.Cursor:
	return request(f"INSERT INTO {table} VALUES {values}", False)
	
	
def delete(table:str, condition:str)->sqlite3.Cursor:
	return request(f"DELETE FROM {table} WHERE {condition}", False)


def select(table:str, value:str)->sqlite3.Cursor:
	return request(value, True)
	

def update(table:str, ):
	pass
	

def request(value:str, verbose:bool)->sqlite3.Cursor:
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	
	rows = cursor.execute(value)
	if verbose:
		for row in rows:
			print(f"\n{row}")
	db.commit()
	db.close()
	return rows	



def populate(filename:str, name:str)->None:
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			#insert(name, (row[0], float(row[1]), float(row[2])))
			insert(name, (row[0], row[1], f"{row[2]} {row[3]}", row[4], row[5], row[6], row[7], row[8], row[9], float(row[10]), float(row[11])))	
				
		
if __name__ == "__main__":
	
	table = "Location"
	
	# UPDATE Customers SET ContactName = 'Alfred Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;
	
	"""
	drop(table)
	create(table,"Hash, Name, Address, Town, Municipality, Department, Region, Postcode, Country, Latitud, Longitud")
	
	with open("/home/ksys/Documents/Project3/data/deparments.txt", encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for filename in reader:
			filename = f"/home/ksys/Documents/Project3/data/{filename[0]}/{filename[0]}.csv"
			print(f"\033[34m{filename}\033[00m")
			populate(filename, table)
			select(table, f"SELECT DISTINCT Department FROM {table}")
			#input()
	"""
	
	# Pays, Region, Department, Town
	select(table, '''SELECT * FROM Location WHERE Region="Provence-Alpes-Côte d'Azur"''')


	"""
	insert(table, ('Addr1', 100, 200.4))
	select(table, f"SELECT * FROM {table}")
	delete(table, "Address = 'Addr1'")
	select(table, f"SELECT * FROM {table}")
		
	drop(table)
	"""	


