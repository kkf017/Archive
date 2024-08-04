import flask

from services.config import * 
from services.users.management import *

@app.route("/place/like", methods=['GET','POST'])
def place1()->str:
	uid = flask.request.args.get('uid')
	ids = flask.request.args.get('id')
	# add Like in database - Table
	favorites(uid, ids)
	# change hash also for FAVORITES (table) - while updating email
	return flask.redirect(flask.url_for("location4", uid = uid, id = ids))

