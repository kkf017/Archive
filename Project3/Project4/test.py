

from services.users.databasebis import *



if __name__ == "__main__":

	
	new = "Hibiscus712"
	hashs = "20ff53268a2d027f3825ca02b17bd85e61a68e14"	
	value = f'''UPDATE {TABLEUSER} SET Username = "{new}" WHERE Hash = "{hashs}";'''	
	x = request(value, False)
	
	print(x)

	for x in select(TABLEUSER, f'''SELECT * FROM {TABLEUSER}'''):
		print("\n",x)
	
