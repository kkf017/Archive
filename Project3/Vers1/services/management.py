from services.databasebis import *

from typing import Tuple

def getUser(email:str, password:str)->str:
	x = select(TABLEUSER, f'''SELECT * FROM {TABLEUSER} WHERE Email="{email}"''')
	for row in x:
		if row[3] == UHASH(password):
			return row[0]
	return ""

	

def exists(key:str, value:str, *args:Tuple[str])->bool:
	x = select(TABLEUSER, f'''SELECT * FROM {TABLEUSER} WHERE {key}="{value}"''')
	if key == "Email" and args != ():
		for row in x:
			if row[2] == args[0]:
				return True
				
	if (key == "Email" and args == ()) or (key == "Username"):
		if x != []:
			return True

	return False



def addUser(email:str, username:str, password:str)->None:
	insert(TABLEUSER, (UHASH(email), email, username, UHASH(password)))

