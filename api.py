from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'random string'

@app.route("/home")
def index():
	if("username" in session.keys()):
		return render_template('welcome.html', login="True")
	else:
		return render_template('welcome.html', login="False")



@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))



@app.route("/products")
def products():
	if("username" in session.keys()):
		return render_template('products.html')
	else:
		return redirect(url_for('index'))


@app.route("/search")
def search():
	if("username" in session.keys()):
		search_query = request.args.get("search")
		print (search_query)
		products = ["apple", "banana", "tomato"]
		if search_query in products:
			return render_template('search_results.html', products=search_query)
	else:
		return redirect(url_for('index'))
	
	


@app.route("/login", methods=['POST'])
def login():
	username = request.form["username"]
	if(username == "Rahul" and request.form["password"] == "rahulp"):
		print("Login succesful, showing you the project page")
		session['username'] = username
		return redirect(url_for('index'))
	else:
		return render_template('error.html')



if(__name__ == "__main__"):
	app.run(port=4000)
