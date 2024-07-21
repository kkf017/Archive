import flask

from services.config import * 
from services.management import *


@app.route("/home/", methods=['GET','POST'])
def hello()->str:	
	return flask.redirect(flask.url_for("login")) #flask.render_template("home-bis.html", msg="")
