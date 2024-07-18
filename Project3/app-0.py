import flask

from services.config import * 
from services.calculation import *

#https://www.boites-a-livres.fr/
#https://boite.a.livres.zonelivre.fr/boites-a-livres-par-departements/


@app.route("/")
def home()->str:
	# remove all files from ../static/maps	
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
def SearchPlace()->str:
	result = searchID(flask.request.args.get('id'))
	return flask.render_template("place.html", result = result[0])
	
@app.route("/request/place", methods=['POST'])
def RequestPlace()->str:
	result = searchID(flask.request.args.get('id'))
	return flask.render_template("place.html", result = result[0])
	
@app.route("/location/place", methods=['POST'])
def locationPlace()->str:
	result = searchID(flask.request.args.get('id'))
	return flask.render_template("place.html", result = result[0])




@app.route("/contact/", methods=['POST'])
def contact()->str:
	return flask.render_template("contact.html")
	
@app.route("/send/", methods=['POST'])
def send()->str:
	return flask.render_template("unknown.html")

@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")	
	
@app.route("/location/unknown", methods=['POST'])
def locationUnknown()->str:
	print(searchID(flask.request.args.get('id')))
	return flask.render_template("unknown.html")

	
	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
