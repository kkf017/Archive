from services.users.databasebis import *

from typing import Tuple, Dict

def getUser(email:str, password:str)->str:
	x = select(TABLEUSER, f'''SELECT * FROM {TABLEUSER} WHERE Email="{email}"''')
	for row in x:
		if row[3] == UHASH(password):
			return row[0]
	return ""


def getUserInfo(key:str, value:str)->Dict[str, str]:
	x = select(TABLEUSER, f'''SELECT * FROM {TABLEUSER} WHERE {key}="{value}"''')
	user = {}
	if x != []:
		x = x[0]
		user["hash"] = x[0]
		user["email"] = x[1]
		user["username"] = x[2]
		user["password"] = x[3]
	return user
	
	

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

def updateUser(uid:str, key:str, value:str)->str:
	res = uid
	x = f'''UPDATE {TABLEUSER} SET {key} = "{value}" WHERE Hash = "{uid}";'''
	if key == "Email":
		new = UHASH(value)
		x = f'''UPDATE {TABLEUSER} SET {key} = "{value}", Hash = "{new}" WHERE Hash = "{uid}";'''
		res = new
	if key == "Password":
		new = UHASH(value)
		x = f'''UPDATE {TABLEUSER} SET {key} = "{new}" WHERE Hash = "{uid}";'''
	x = request(x, False)
	return res

