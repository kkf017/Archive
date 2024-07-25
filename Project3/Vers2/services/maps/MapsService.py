import flask

from services.config import * 
from services.maps.calculation import *



@app.route("/location", methods=['GET','POST'])
def location()->str:		
	if flask.request.method == 'POST':	
		result = sphere(flask.request.form["search-addr"], float(flask.request.form["search-radius"]))
		
	if flask.request.args.get('uid') != None:
		value = {}
		value["uid"] = flask.request.args.get('uid')
		value["result"] = result
		return flask.render_template("./profil/profil-location.html", value = value)
		
	return flask.render_template("location.html", result = result)
	

@app.route("/search/", methods=['GET','POST']) # search
def search()->str:
	result = {}
	if flask.request.method == 'POST':	
		result = fill()
	if flask.request.args.get('uid') != None:
		value = {}
		value["uid"] = flask.request.args.get('uid')
		value["result"] = result
		return flask.render_template("./profil/profil-search.html", value = value)
	return flask.render_template("search.html", result = result)	


@app.route("/request", methods=['GET','POST'])
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
	if flask.request.args.get('uid') != None:
		value = {}
		value["uid"] = flask.request.args.get('uid')
		value["result"] = result
		return flask.render_template("./profil/profil-request.html", value = value)
		
	return flask.render_template("request.html", result = result)
	


@app.route("/search/place", methods=['GET','POST'])
def SearchPlace()->str:
	if flask.request.args.get('uid') != None:
		return f"Hello from SearchPlace user {flask.request.args.get('uid')} & place {flask.request.args.get('id')}"
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
	
	
@app.route("/place", methods=['GET','POST'])
def placeUI()->str:
	result = searchID(flask.request.args.get('id'))
	if flask.request.args.get('uid') != None:
		value = {}
		value["uid"] = flask.request.args.get('uid')
		value["result"] = result[0]
		return flask.render_template("./profil/profil-place.html", value = value)
	return flask.render_template("place.html", result = result[0])


@app.route("/contact/", methods=['GET','POST'])
def contact()->str:
	uid = ""
	if flask.request.args.get('uid') != None:
		uid = flask.request.args.get('uid')
		return flask.render_template("./profil/profil-contact.html", uid=uid)
	return flask.render_template("contact.html", uid=uid)
	
@app.route("/send/", methods=['POST'])
def send()->str:
	return flask.render_template("unknown.html")

@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")	
	
@app.route("/location/unknown", methods=['POST'])
def locationUnknown()->str:
	return flask.render_template("unknown.html")
