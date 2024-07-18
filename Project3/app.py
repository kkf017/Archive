import flask

from services.config import * 
from services.management import *


@app.route("/")
def home()->str:
	# remove all files from ../static/maps	
	return flask.render_template("home-bis.html", display=[1]
	)


@app.route("/login/", methods=['POST'])
def login()->str:
	username = flask.request.form["Username"]
	email = flask.request.form["Email"]
	password = flask.request.form["password"]
	check = flask.request.form["password-check"]
	acc = flask.request.form.get("createAccount")
		
	# Create account
	if check=="on":
		if not password == check:
			pass
		# add to database
		pass
	# Login	
	else:
		# check if email-username in database
		# login with password
		pass
	
	return flask.render_template("home-bis.html")

if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
