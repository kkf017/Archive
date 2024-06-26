import os
import csv

from typing import Tuple, Union

def readtxt(filename:str)->None:
	""" Function to read a .txt file. """
	if os.path.exists(f"{filename}.csv"):
		os.remove(f"{filename}.csv")
			
	if os.path.exists(f"{filename}-err.csv"):
		os.remove(f"{filename}-err.csv")
		
	with open(f"{filename}.txt", 'r') as f:
		for line in f.readlines():
			add(filename, line)

def readCSV(filename:str)->None:
	""" Function to read a .csv file. """
	with open(filename, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=';')
		for row in reader:
			print(f"\n\n{row[0]} \n{row[1]},{row[2]}")			
			
def writeCSV(filename:str, *args:Tuple[Union[str, float]])->None:
	""" Function to write .csv file. """		
	with open(filename, 'a', encoding='utf8') as fp:
        	writer = csv.writer(fp, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
        	writer.writerow(args)


def add(filename:str, x:str)->None:
	""" Function to commit ... """	
	addr, latitud, longitud = coordinates(x)
	
	if not(addr == None and latitud == None and longitud == None):
		print(f"\n\n{x} {addr} \n{latitud}, {longitud}")
		writeCSV(f"{filename}.csv", addr, latitud, longitud)
	else:
		print(f"\n\nERREUR !! - {x}")
		writeCSV(f"{filename}-err.csv", x)
		

if __name__ == "__main__":

	filename = "Ain"
	#readtxt(filename)
	readCSV(f"{filename}.csv")
