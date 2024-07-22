import flask

from services.config import * 
from services.maps.calculation import *

from services.maps.MapsService import *
from services.users.UserLoginService import *
from services.users.UserAccountService import *

#https://www.boites-a-livres.fr/
#https://boite.a.livres.zonelivre.fr/boites-a-livres-par-departements/


# manage PATH of database - geographic.db, users.db (move file)


# RESTRUCT code - with comments (organize)
 

@app.route("/")
def home()->str:
	# remove all files from ../static/maps	
	return flask.render_template("home.html")	

	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
