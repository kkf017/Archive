import os
import copy
from urllib.request import urlopen
import bs4

# pip install beautifulsoup4
# pip install regex

FOLDER = "/home/ksys/Documents/Project3/data/"
EXCEPT = ["dordogne", "https://www.boites-a-livres.fr/ville/aigre/16140", "https://www.boites-a-livres.fr/ville/aigre/16140","https://www.boites-a-livres.fr/ville/ailhon/07200", "https://www.boites-a-livres.fr/ville/magnieu/01300", "https://www.boites-a-livres.fr/ville/moulins/03000", "https://www.boites-a-livres.fr/ville/bazeilles/08140", "https://www.boites-a-livres.fr/ville/saint-bonnet-de-rochefort/03800", "https://www.boites-a-livres.fr/ville/isigny-sur-mer/14230", "https://www.boites-a-livres.fr/ville/rots/14980", "https://www.boites-a-livres.fr/ville/murat/15300", "https://www.boites-a-livres.fr/ville/confolens/16500", "https://www.boites-a-livres.fr/ville/vergeroux/17300", "https://www.boites-a-livres.fr/ville/dinan/22100", "https://www.boites-a-livres.fr/ville/jugon-les-lacs-commune-nouvelle/22270", "https://www.boites-a-livres.fr/ville/etalans/25580", "https://www.boites-a-livres.fr/ville/les-premiers-sapins/25580", "https://www.boites-a-livres.fr/ville/levier/25270", "https://www.boites-a-livres.fr/ville/chatillon-en-diois/26410", "https://www.boites-a-livres.fr/ville/pacy-sur-eure/27120", "https://www.boites-a-livres.fr/ville/langeais/37130"]



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
		def get_text_1(html):
			soup = bs4.BeautifulSoup(html) 
			for li in soup.findAll('ul'):
				if not li == None:
					for x in soup.findAll('li'):
						if "Adresse approximative" in x.text:
							return x.text.split(":")[1][1:]
			return None
		
		def finditall(msg):	
			def findit(sub):
				first = sub.find('.bindPopup("<small><a href=')
				last =  sub.find(">Voir la fiche détaillée</a></small>")
				if first == -1:
					return (None, None)
				#print(sub[first+len('.bindPopup("<small><a href=')+1: last][:-1])
				return (first+len('.bindPopup("<small><a href=')+1, last)
			
			res = []
			while 1:
				x, y = findit(msg)
				if x == None and y == None:
					break
				res.append(msg[x:y][:-1])
				msg = copy.copy(msg[y+len(">Voir la fiche détaillée</a></small>"):])
			return res
			
		with open(f"{FOLDER}{filename}/{filename}.txt", 'w') as writer:	
			with open(f"{FOLDER}{filename}/{filename}-link.txt", 'r') as f:
				for line in f.readlines():
					print(f"\n\n--->\033[34m{line}\033[00m")
					
					if not line in EXCEPT:
						page = urlopen(line)
						html = page.read()
						html = html.decode("utf-8")
					
						x = get_text_1(html)
						if not x == None:
							print(x)
							writer.write(x+"\n")
						else:
							soup = bs4.BeautifulSoup(html) 
							for li in soup.findAll('script', {"type": "text/javascript"}):
								res = finditall(li.text)
								for i in res:
									page = urlopen(i)
									html = page.read()
									html = html.decode("utf-8")
									x = get_text_1(html)
									print(x)
									writer.write(x+"\n")
				
				
	with open(filename, 'r') as f:
		for line in f.readlines():
			print(f"\033[35m\n\n\n************************************************************\033[00m")
			print(f"\033[35m {FOLDER}{line[:-1]}/{line[:-1]}-link.txt\033[00m")
			print(f"\033[35m************************************************************\033[00m")
			link(line[:-1]) #f"{FOLDER}{line[:-1]}/{line[:-1]}-link.txt")
			input()
	

if __name__ == "__main__":

	#get_municipality("deparments-link.txt")
	get_place("deparments.txt")
