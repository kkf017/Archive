import flask

from services.config import * 

@app.route("/")
def home()->str:	
	return flask.render_template("home.html")
	

if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
