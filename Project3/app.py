import flask

from services.config import * 

@app.route("/")
def home()->str:	
	return flask.render_template("home.html")


@app.route("/home/", methods=['POST'])
def home2()->str:	
	return "Helo,from home !"	


@app.route("/search/", methods=['GET','POST'])
def search()->str:
	if flask.request.method == 'POST':	
		x = flask.request.form["search-radius"]
		text = flask.request.form["searchAddr"]
		print(text)
	return f"Helo,from search-place {text}, {x}!"
	
	
@app.route("/all/",  methods=['POST'])
def allBB()->str:	
	return "Helo,from all Book Boxes !"
	
	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
