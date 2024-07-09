import os
from urllib.request import urlopen
import bs4

# pip install beautifulsoup4

FOLDER = "/home/ksys/Documents/Project3/data/"
EXCEPT = ["dordogne"]



def get_departments(url):
	url = "https://www.boites-a-livres.fr/departements"
	page = urlopen(url)
	html = page.read()
	html = html.decode("utf-8")
	
	# get list of departments
	soup = bs4.BeautifulSoup(html)
	for link in soup.findAll("a"):
		print(link.get("href"))
		

def get_municipality(filename):
	def link(url):
		page = urlopen(url)
		html = page.read()
		html = html.decode("utf-8")

		name = url.split("/")[-1][:-1]
		if not name in EXCEPT:
			os.mkdir(f"{FOLDER}{name}")
			print(f"\n\n\n{name}")
			soup = bs4.BeautifulSoup(html)
			with open(f"{FOLDER}{name}/{name}-link.txt", 'w') as f:
				i = 0
				for link in soup.findAll("a"):
					x = link.get("href")
					if not (i==0 or i == 1 or "https://www.boites-a-livres.fr/ajout/" in x or x in ["https://openstreetmap.org/copyright", "https://library.love/@boitesalivres", "https://www.facebook.com/profile.php?id=61551465693450"]):
						f.write(x+"\n")
					i+=1
			print("End.")
		
	with open(filename, 'r') as f:
		for line in f.readlines():
			link(line) # deparments-link.txt
	


def get_place(filename):
	def link(filename):
		with open(filename, 'r') as f:
			for line in f.readlines():
				print(line)
				
				page = urlopen(line)
				html = page.read()
				html = html.decode("utf-8")
				print(html)
				
				# find address - write in .txt file
				input()
				
				
	with open(filename, 'r') as f:
		for line in f.readlines():
			print(f"\n\n\n{FOLDER}{line[:-1]}/{line[:-1]}-link.txt")
			link(f"{FOLDER}{line[:-1]}/{line[:-1]}-link.txt")
	

if __name__ == "__main__":

	#get_municipality("deparments-link.txt")
	get_place("deparments-name.txt")

	#for each link in department.txt
		# create folder
		# create .txt
