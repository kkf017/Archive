import flask

from services.config import * 

# Find it by yourself ! Get the full list of book boxes.
# Add ur own place ! You want to particpate ? Give the address of the closest book box to you.
# List of books per place - add/remove
# Exchange

# https://stackoverflow.com/questions/69980212/flask-javascript-array-display-in-html
#https://stackoverflow.com/questions/62682674/how-to-get-dynamic-html-table-entries-in-a-form-to-flask
#https://stackoverflow.com/questions/62682674/how-to-get-dynamic-html-table-entries-in-a-form-to-flask


@app.route("/")
def home()->str:	
	return flask.render_template("home.html")	


@app.route("/search/", methods=['GET','POST'])
def search()->str:
	if flask.request.method == 'POST':	
		x = flask.request.form["search-radius"]
		text = flask.request.form["search-addr"]
		print(text, x)
		# check if place exist
		# if not text exist:
			# Html, Error
	result = [{"filed1": "klfsnö", "filed2":45.54}, {"filed1": "oprjeg", "filed2":54.2564}]
	return flask.render_template("search.html", result = result)
	
	
	
if __name__ == "__main__":

	app.run(debug=True)
	#app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 4444)))
