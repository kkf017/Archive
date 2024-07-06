import flask

from services.config import * 
from services.calculation import sphere, fill, filters

#https://www.boites-a-livres.fr/
#https://boite.a.livres.zonelivre.fr/boites-a-livres-par-departements/

# Find it by yourself ! Get the full list of book boxes.
# Add ur own place ! You want to particpate ? Give the address of the closest book box to you.
# add geolocation - find the closest box .. your geolocation
# List of books per place - add/remove
# Exchange

# Check and complete data - for database


# Check ... for urls.


# https://stackoverflow.com/questions/55818303/show-location-of-coordinates-on-google-maps-using-python
# folium - https://stackoverflow.com/questions/72249181/how-to-insert-points-in-a-map

@app.route("/")
def home()->str:	
	return flask.render_template("home.html")	


@app.route("/search/", methods=['GET','POST'])
def search()->str:
	if flask.request.method == 'POST':	
		result = sphere(flask.request.form["search-addr"], float(flask.request.form["search-radius"]))
	return flask.render_template("search.html", result = result)
	

@app.route("/list/", methods=['POST'])
def list()->str:
	if flask.request.method == 'POST':	
		result = fill()	
	return flask.render_template("list.html", result = result)	


@app.route("/filter/", methods=['POST'])
def filter()->str:
	key, value = (None, None)

	if not flask.request.form["filter-country"] == "None":
		key, value = ("Country", flask.request.form["filter-country"])

	if not flask.request.form["filter-region"] == "None":
		key, value = ("Region", flask.request.form["filter-region"])	
		
	if not flask.request.form["filter-department"] == "None":
		key, value = ("Department", flask.request.form["filter-department"])	
	
	if not flask.request.form["filter-town"] == "None":
		key, value = ("Town", flask.request.form["filter-town"])

	result = filters(key, value)
	return flask.render_template("list.html", result = result)

@app.route("/bookbox/", methods=['POST'])
def bookbox()->str:
	return flask.render_template("bookbox.html")
	
	
@app.route("/getmap/", methods=['POST'])
def getmap()->str:
	return flask.render_template("map.html")

@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")	

	
	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
