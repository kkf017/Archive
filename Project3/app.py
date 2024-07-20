import flask

from services.config import * 
from services.management import *


@app.route("/")
def home()->str:
	# remove all files from ../static/maps	
	return flask.render_template("home-bis.html", display=[1])


@app.route("/login/", methods=['POST'])
def login()->str:
	email = flask.request.form["Email"]
	password = flask.request.form["password"]
	flag = getUser(email, password)
	if flag == False:
		return flask.render_template("home-bis-error.html")
	return flask.render_template("home-bis.html")


@app.route("/register/", methods=['POST'])
def registration()->str:
	return flask.render_template("register.html")

@app.route("/registration/", methods=['POST'])
def registrationbis()->str:
	username = flask.request.form["Username"]
	email = flask.request.form["Email"]
	password = flask.request.form["password"]
	check = flask.request.form["password-check"]
	print(username, email, password, check)
	# check if already exists in database
		# search on email - check if username ==
		# search on username - check if username ==
	# check if password == check
	# add email verification
	return flask.render_template("register.html")
	
	
	

@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")

if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
