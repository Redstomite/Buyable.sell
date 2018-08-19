from flask import Flask, request, render_template, redirect, url_for, session
import pdb, random
from models.user_model import user_signup, search_user_by_username
from models.product_model import product_add

app = Flask(__name__)
app.secret_key = 'random string'

@app.route("/home")
def index():
	if("user_id" in session.keys()):
		return render_template('welcome.html', login="True")
		if(request.form["accounttype"] == "isavendor"):
			return render_template('welcome.html', login="True", vendor="True")
	else:
		return render_template('welcome.html', login="False")




@app.route("/signup", methods=['GET'])
def showpage():
	return render_template('signup.html')	

@app.route("/signup", methods=['POST'])
def signup():
	user_info = {}
	user_info["username"] = request.form["username"]
	user_info["password"] = request.form["password"]
	user_info["email"] = request.form["email"]
	user_info["phonenum"]  = request.form["phonenum"]
	user_info["firstname"] = request.form["firstname"]
	user_info["lastname"] = request.form["lastname"]
	user_info["accounttype"] = request.form["vendoraccount"]
	if (user_info["username"] or user_info["password"] or user_info["email"] or user_info["phonenum"] or user_info["firstname"] or user_info["lastname"] != ""):
		results = user_signup(user_info)
		if (results is True):
			session['user_id'] = str(user_info['id'])
		return("Saved!")
	else:
		return render_template('signuperror.html')



@app.route("/addproduct", methods=['GET'])
def addproduct():
	return render_template('addproduct.html')

@app.route("/addproduct", methods=['GET', 'POST'])
def handle_addproduct():
	
	if("user_id" in session.keys()):
	#	pdb.set_trace()
		product_info = {}
		product_info["productname"] = request.form["productname"]
		product_info["productprice"] = request.form["productprice"]
		product_info["producttype"] = request.form["producttype"]
		product_info["productquantity"] = request.form["productquantity"]
		
		if(product_info["productname"] or product_info["productprice"] or product_info["producttype"] or product_info["productquantity"] != ""):
			productkeyascii = []
			for x in range(1,6):
				random_ascii= random.randint(64, 126)
				productkeyascii.append(random_ascii)
			productkeylist = []
			for item in productkeyascii:
				chr(item)
				print(item)
				productkeylist.append(item)
			print(productkeylist)
			productkey = ''.join(str(productkeylist))
			product_info["productkey"] = productkey
			productInformation = product_add(product_info)
			return redirect(url_for('products'))
		else:
			print("Complete the entire form.")
	else:
		return redirect(url_for('index'))



@app.route('/logout')
def logout():
   session.pop('user_id', None)
   return redirect(url_for('index'))




@app.route("/products")
def products():
	if("user_id" in session.keys()):
		return render_template('products.html')
	else:
		return redirect(url_for('index'))




@app.route("/search")
def search():
	if("user_id" in session.keys()):
		search_query = request.args.get("search")
		print (search_query)
		products = ["apple", "banana", "tomato"]
		if search_query in products:
			return render_template('search_results.html', products=search_query)
	else:
		return redirect(url_for('index'))
	

	

@app.route("/login", methods=['POST'])
def login():
	inbound_username = request.form["username"]
	existing_user = search_user_by_username(inbound_username)
	if(existing_user is None):
		return render_template('signuperror.html')
	elif(request.form["password"] == existing_user["password"]):
		print("Login succesful, showing you the project page")
		session['user_id'] = str(existing_user['_id'])
		return redirect(url_for('index'))
	else:
		return render_template('loginerror.html')



if(__name__ == "__main__"):
	app.run(port=4000)










