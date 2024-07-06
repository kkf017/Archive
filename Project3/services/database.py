import csv
import sqlite3

from typing import Tuple, Optional, Any


DATABASE = 'geographic.db'
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

	
				
		
if __name__ == "__main__":
	
	table = "Location"
	
	#drop(table)
	#create(table, "Address, Latitud, Longitud")
	#create(table,"Hash, Name, Address, Town, Municipality, Department, Region, Postcode, Country, Latitud, Longitud")

	
	select(table, "SELECT DISTINCT Town FROM Location ORDER BY Town;")


	"""
	insert(table, ('Addr1', 100, 200.4))
	select(table, f"SELECT * FROM {table}")
	delete(table, "Address = 'Addr1'")
	select(table, f"SELECT * FROM {table}")
		
	drop(table)
	"""	


