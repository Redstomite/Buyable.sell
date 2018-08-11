from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/home")
def index():
	return render_template('welcome.html')

@app.route("/products")
def products():
	username = request.args["username"]
	return render_template('products.html', username=username)
	
@app.route("/login", methods=['POST'])
def login():
	username = request.form["username"]
	if(username == "Rahul" and request.form["password"] == "rahulp"):
		print("Login succesful, showing you the project page")
		return redirect(url_for('products', username=username))
	else:
		return render_template('error.html')
if(__name__ == "__main__"):
	app.run(port=4000)
