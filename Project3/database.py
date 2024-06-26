import sqlite3

from typing import Tuple, Optional, Any

#https://docs.python.org/3.8/library/sqlite3.html

DATABASE = 'geographic.db'

def drop(table:str)->sqlite3.Cursor:
	return request(f"DROP TABLE IF EXISTS {table};")
	

def create(table:str, columns:str)->sqlite3.Cursor:
	drop(table)
	return request(f"CREATE TABLE {table} ({columns})")
	
	
def insert(table:str, values:Tuple[Any])->sqlite3.Cursor:
	return request(f"INSERT INTO {table} VALUES {values}")
	
	
def delete(table:str, condition:str)->sqlite3.Cursor:
	return request(f"DELETE FROM {table} WHERE {condition}")


def select(table:str, value:str)->sqlite3.Cursor:
	return request(value)
	"""
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	rows = cursor.execute(request)
	print("\n\n")
	for row in cursor.execute(f"SELECT * FROM {TABLE}"):
		print(row)
	db.commit()
	db.close()
	"""

def request(value:str)->sqlite3.Cursor:
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	
	rows = cursor.execute(value)
	print("\n\n")
	for row in rows:
		print(row)
	
	db.commit()
	db.close()
	return rows
	
	
if __name__ == "__main__":
	
	table = "Location"
	
	drop(table)
	create(table, "Address, Latitud, Longitud")
	select(table, f"SELECT * FROM {table}")
	
	"""
	insert(table, ('Addr1', 100, 200.4))
	select(table, f"SELECT * FROM {table}")
	delete(table, "Address = 'Addr1'")
	select(table, f"SELECT * FROM {table}")
		
	drop(table)
	"""	


