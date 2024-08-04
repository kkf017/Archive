from services.users.databasebis import *

from typing import Tuple, Dict

def getUser(email:str, password:str)->str:
	x = select(USERS, f'''SELECT * FROM {USERS} WHERE Email="{email}"''')
	for row in x:
		if row[3] == HASH(password):
			return row[0]
	return ""


def getUserInfo(key:str, value:str)->Dict[str, str]:
	x = select(USERS, f'''SELECT * FROM {USERS} WHERE {key}="{value}"''')
	user = {}
	if x != []:
		x = x[0]
		user["hash"] = x[0]
		user["email"] = x[1]
		user["username"] = x[2]
		user["password"] = x[3]
	return user
	
	

def exists(key:str, value:str, *args:Tuple[str])->bool:
	x = select(USERS, f'''SELECT * FROM {USERS} WHERE {key}="{value}"''')
	if key == "Email" and args != ():
		for row in x:
			if row[2] == args[0]:
				return True
				
	if (key == "Email" and args == ()) or (key == "Username"):
		if x != []:
			return True

	return False



def addUser(email:str, username:str, password:str)->None:
	insert(USERS, (HASH(email), email, username, HASH(password)))

def updateUser(uid:str, key:str, value:str)->str:
	def UpdateUsername(uid:str, key:str, value:str)->str:
		x = f'''UPDATE {USERS} SET {key} = "{value}" WHERE Hash = "{uid}";'''
		x = request(x, False)
		return uid
		
	def UpdateEmail(uid:str, key:str, value:str)->str:
		new = HASH(value)
		x = f'''UPDATE {USERS} SET {key} = "{value}", Hash = "{new}" WHERE Hash = "{uid}";'''
		# change hash also for FAVORITES (table)
		x = request(x, False)
		x = f'''UPDATE {FAVORITES} SET {User} = "{new}" WHERE Hash = "{uid}";'''
		x = request(x, False)
		return new
		
	def UpdatePassword(uid:str, key:str, value:str)->str:
		new = HASH(value)
		x = f'''UPDATE {USERS} SET {key} = "{new}" WHERE Hash = "{uid}";'''
		x = request(x, False)
		return uid

	if key == "Email":
		return UpdateEmail(uid, key, value)
	if key == "Password":
		return UpdatePassword(uid, key, value)
	return UpdateUsername(uid, key, value)


def favorites(uid:str, ids:str)->None:
	insert(FAVORITES, (uid, ids))
