import flask

from services.config import * 
from services.management import *


@app.route("/uids/", methods=['GET','POST'])
def uid()->str:	
	return flask.render_template("search-acc.html", result = []) #flask.redirect(flask.url_for("login")) #flask.render_template("home-bis.html", msg="")
	
	

@app.route("/uid", methods=['GET','POST']) # search
def homeAcc()->str:
	result = flask.request.args.get('id')
	user = {}
	user = getUserInfo(result)
	return flask.render_template("search-acc.html", user = user)
