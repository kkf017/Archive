from services.databasebis import *


def getUser(email:str, password:str)->bool:
	value = f'''SELECT * FROM {TABLE} WHERE Email="{email}"'''
	db = sqlite3.connect(DATABASE)
	cursor = db.cursor()
	rows = cursor.execute(value)
	for row in rows:
		if row[3] == HASH(password):
			return True
	db.commit()
	db.close()
	return False
