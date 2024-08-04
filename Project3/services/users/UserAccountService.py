import flask

from services.config import * 
from services.maps.calculation import *
from services.users.management import *



@app.route("/acc", methods=['GET','POST'])
def account()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/profil?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	user = getUserInfo("Hash",uid)
	return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-user-bis.html"), user = user)			
	#return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-user.html"), user = user)
	

@app.route("/acc/user", methods=['GET','POST'])
def account1()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/acc/user?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	user = getUserInfo("Hash",uid)			
	return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-user-updt-username.html"), user = user)

@app.route("/acc/user/updt", methods=['GET','POST'])
def account4()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/acc/user/updt?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	uid = updateUser(uid, "Username", flask.request.form["new-username"])	
	user = getUserInfo("Hash", uid)
	return flask.redirect(flask.url_for("account", uid = user["hash"]))
		


@app.route("/acc/email", methods=['GET','POST'])
def account2()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/acc/email?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	user = getUserInfo("Hash",uid)			
	return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-user-updt-email.html"), user = user)


@app.route("/acc/email/updt", methods=['GET','POST'])
def account5()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/acc/email/updt?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	#email1 = flask.request.form["new-email"]
	#email2 = flask.request.form["verif-email"]
	#if email1 != email2:
		#return f"Hello from UPDT Email, with {email1} and {email2}" 
		
	# Verify email - (with email verification)
	
	uid = updateUser(uid, "Email", flask.request.form["new-email"])	
	user = getUserInfo("Hash", uid)
	return flask.redirect(flask.url_for("account", uid = user["hash"]))


	

@app.route("/acc/password", methods=['GET','POST'])
def account3()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/acc/password?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	user = getUserInfo("Hash", uid)			
	return flask.render_template(os.path.join(TEMPLATE, "/profil/profil-user-updt-password.html"), user = user)
	

@app.route("/acc/password/updt", methods=['GET','POST'])
def account6()->str:
	""" 
		(URL):
			http://127.0.0.1:5000/acc/password/updt?uid=daaab105702e8d6ffd23ad6f0f7a50de4c0eda8b
	"""	
	uid = flask.request.args.get('uid')
	password1 = flask.request.form["new-password"]
	password2 = flask.request.form["verif-password"]
	if password1 != password2:
		return f"Hello from UPDT Email, with {password1} and {password2}"
		
	uid = updateUser(uid, "Password", flask.request.form["new-password"])	
	user = getUserInfo("Hash", uid)
	return flask.redirect(flask.url_for("account", uid = user["hash"]))	


