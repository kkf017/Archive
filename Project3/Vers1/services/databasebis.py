import os.path
import csv
import sqlite3
import hashlib

from .config import PATH

from typing import List, Tuple, Optional, Any

UHASH = lambda x: (hashlib.sha1(x.encode())).hexdigest()

DATABASEUSER = os.path.join(PATH, "users.db")
TABLEUSER = "Users"

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
	

def request(value:str, verbose:bool)->List[Tuple[Any]]: #sqlite3.Cursor:
	db = sqlite3.connect(DATABASEUSER)
	cursor = db.cursor()
	
	rows = cursor.execute(value)
	x = list(rows)
	#if verbose:
		#for row in rows:
			#print(f"\n{row}")
	
	db.commit()
	db.close()
	return x	


	
		
if __name__ == "__main__":

	
	"""
	drop(TABLEUSER)
	create(TABLEUSER,"Hash, Email, Username, Password")

	username = "smililly"
	email = "smililly@yahoo.com"
	password = "smililly<3LOVEsU"
	insert(TABLEUSER, (UHASH(email), email, username, UHASH(password)))
	
	
	username = "summer85"
	email = "summer.85@yahoo.com"
	password = "summer:)85"
	insert(TABLEUSER, (UHASH(email), email, username, UHASH(password)))
	"""
	
	# Pays, Region, Department, Town
	select(TABLEUSER, f'''SELECT * FROM {TABLEUSER}''')

"""
	insert(TABLE, ('Addr1', 100, 200.4))
	select(TABLE, f"SELECT * FROM {table}")
	delete(TABLE, "Address = 'Addr1'")
	select(TABLE, f"SELECT * FROM {table}")
		
	drop(TABLE)
"""	


