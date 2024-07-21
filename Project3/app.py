import flask

from services.config import * 
from services.management import *


@app.route("/")
def home()->str:
	# remove all files from ../static/maps	
	return flask.render_template("home-bis.html", msg="")
	

@app.route("/login/", methods=['GET','POST'])
def login()->str:
	if flask.request.method == 'POST':
		email = flask.request.form["Email"]
		password = flask.request.form["password"]
		flag = getUser(email, password)
		if flag == "":
			return flask.render_template("home-bis.html", msg="Email, or password not valid.")
			
		# add forget your password ?
		return flask.redirect(flask.url_for("user", idt=flag))
		 
	return flask.render_template("home-bis.html", msg="")




@app.route("/user/<idt>", methods=['GET','POST'])
def user(idt:str)->str:
	return flask.render_template("home-profil.html", msg="")



@app.route("/register/", methods=['POST'])
def registration()->str:
	return flask.render_template("register.html", msg="")
	

@app.route("/registration/", methods=['POST'])
def registrationbis()->str:
	def check():
		pass
	username = flask.request.form["Username"]
	email = flask.request.form["Email"]
	password = flask.request.form["password"]
	check = flask.request.form["password-check"]

	if exists("Email", email, username):
		return flask.render_template("register.html", msg="An account already exists.")
	
	if exists("Email", email):
		return flask.render_template("register.html", msg="This email is already used.")
	
	if exists("Username", username):
		return flask.render_template("register.html", msg="This username is already used.")
		
	if not (password == check):
		return flask.render_template("register.html", msg="Password is not valid.")
	
	# add password verification - at least one upper, one digit, one symbol
		
	# add email verification
	
	# add to database
	addUser(email, username, password)
	return flask.render_template("unknown.html", msg="")
	


@app.route("/logout/", methods=['GET','POST'])
def logout()->str:
	return flask.redirect(flask.url_for("login"))	
	

@app.route("/unknown/", methods=['POST'])
def unknown()->str:
	return flask.render_template("unknown.html")
	

if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
