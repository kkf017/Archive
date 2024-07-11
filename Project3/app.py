import flask

from services.config import * 
from services.calculation import *

#https://www.boites-a-livres.fr/
#https://boite.a.livres.zonelivre.fr/boites-a-livres-par-departements/

# Find it by yourself ! Get the full list of book boxes.
# Add ur own place ! You want to particpate ? Give the address of the closest book box to you.
# add geolocation - find the closest box .. your geolocation
# List of books per place - add/remove
# Exchange

# html how to include link to open street maps
# https://blog.hubspot.com/website/how-to-embed-google-map-in-html
# https://webmasters.stackexchange.com/questions/141858/make-a-link-for-an-address-that-opens-the-default-map-app
# https://medium.com/@nargessmi87/how-to-embede-open-street-map-in-a-webpage-like-google-maps-8968fdad7fe4


#https://medium.com/geekculture/how-to-make-a-web-map-with-pythons-flask-and-leaflet-9318c73c67c3

@app.route("/")
def home()->str:	
	return flask.render_template("home.html")	


@app.route("/location/", methods=['GET','POST']) # request
def location()->str:
	if flask.request.method == 'POST':	
		result = sphere(flask.request.form["search-addr"], float(flask.request.form["search-radius"]))
	return flask.render_template("location.html", result = result)
	

@app.route("/search/", methods=['POST']) # search
def search()->str:
	if flask.request.method == 'POST':	
		result = fill()	
	return flask.render_template("search.html", result = result)	


@app.route("/request/", methods=['POST']) # searchit
def request()->str:
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
	return flask.render_template("request.html", result = result)




@app.route("/search/place", methods=['POST'])
def bookboxlist()->str:
	result = searchID(flask.request.args.get('id'))
	markers =[ {'Address': 'THE PLACEs','lat':46.263996, 'lon':6.029845731313132, 'popup':'This is the middle of the map.'}]
	return flask.render_template("BOX.html", result = result[0])
	
@app.route("/request/place", methods=['POST'])
def bookboxfilter()->str:
	result = searchID(flask.request.args.get('id'))
	return flask.render_template("bookbox.html", result = result[0])
	
@app.route("/location/place", methods=['POST'])
def bookboxsearch()->str:
	result = searchID(flask.request.args.get('id'))
	return flask.render_template("bookbox.html", result = result[0])


	
	
@app.route("/getmap/", methods=['POST'])
def getmap()->str:
	return flask.render_template("map.html")

@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")
	#markers =[ {'lat':46.263996, 'lon':6.029845731313132, 'popup':'This is the middle of the map.'}]
	#return flask.render_template("BOX2.html", markers = markers[0])	

	
	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
