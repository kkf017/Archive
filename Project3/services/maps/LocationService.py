import flask

from services.config import * 
import services.users.management

@app.route("/place/like", methods=['GET','POST'])
def place1()->str:
	uid = flask.request.args.get('uid')
	ids = flask.request.args.get('id')
	# add Like in database - Table
	services.users.management.favorites(uid, ids)
	return flask.redirect(flask.url_for("location4", uid = flask.request.args.get('uid'), id = ids))

