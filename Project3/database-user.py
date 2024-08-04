

from services.users.databasebis import *



if __name__ == "__main__":

	
	
	#drop(USERS)
	#create(USERS,"Hash, Email, Username, Password")
	#create(FAVORITES,"User, Location")

	#username = "smililly"
	#email = "smililly@yahoo.com"
	#password = "smililly<3LOVEsU"
	#insert(USERS, (HASH(email), email, username, UHASH(password)))
	
	
	#username = "summer85"
	#email = "summer.85@yahoo.com"
	#password = "summer:)85"
	#insert(USERS, (HASH(email), email, username, UHASH(password)))


	x = select(USERS, f'''SELECT * FROM {USERS}''')
	
	print(x)

	for x in select(USERS, f'''SELECT * FROM {USERS}'''):
		print("\n",x)
		
	print("\n\n\n")
	
	for x in select(FAVORITES, f'''SELECT * FROM {FAVORITES}'''):
		print("\n",x)
	
