import flask

from services.config import * 
from services.management import *


@app.route("/home/", methods=['GET','POST'])
def hello()->str:	
	return flask.redirect(flask.url_for("login")) #flask.render_template("home-bis.html", msg="")
	

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



@app.route("/registration/", methods=['POST'])
def registrationbis()->str:
	return flask.redirect(flask.url_for("register")) 
	

@app.route("/register/", methods=['GET','POST'])
def register()->str:
	def check():
		pass
	
	if flask.request.method == 'POST':	
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
			# https://www.geeksforgeeks.org/password-validation-in-python/
			
		# add email verification
		
		# add to database
		addUser(email, username, password)
		return flask.render_template("unknown.html", msg="")
	return flask.render_template("register.html", msg="")
	


@app.route("/logout/", methods=['GET','POST'])
def logout()->str:
	return flask.redirect(flask.url_for("hello"))	
	

@app.route("/unknown/", methods=['POST'])
def unknownbis()->str:
	return flask.render_template("unknown.html")



