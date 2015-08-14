from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from database_setup import Base, Sports, Equipment, User

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Client id for this app is load from client_secrets.json file
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog Application"

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Generate unique state token to protect from anti forgery attack
@app.route('/login')
def login():
	state = ''.join(random.choice(string.ascii_uppercase + 
		string.digits) for x in range(32))
	login_session['state'] = state
	return render_template('login.html', STATE=state)


# This function is called when sign in button is clicked
@app.route('/gconnect', methods=['POST'])
def gconnect():
	# Validate state token
	if request.args.get('state') != login_session['state']:
		response = make_response(json.dumps('Invalid state parameter.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	# Obtain authorization code
	code = request.data

	try:
	# Upgrade the authorization code into a credentials object
		oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
		oauth_flow.redirect_uri = 'postmessage'
		credentials = oauth_flow.step2_exchange(code)
	except FlowExchangeError:
		response = make_response(
			json.dumps('Failed to upgrade the authorization code.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Check that the access token is valid.
	access_token = credentials.access_token
	url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
	h = httplib2.Http()
	result = json.loads(h.request(url, 'GET')[1])
	# If there was an error in the access token info, abort.
	if result.get('error') is not None:
		response = make_response(json.dumps(result.get('error')), 500)
		response.headers['Content-Type'] = 'application/json'

	# Verify that the access token is used for the intended user.
	gplus_id = credentials.id_token['sub']
	if result['user_id'] != gplus_id:
		response = make_response(
			json.dumps("Token's user ID doesn't match given user ID."), 401)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Verify that the access token is valid for this app.
	if result['issued_to'] != CLIENT_ID:
		response = make_response(
			json.dumps("Token's client ID does not match app's."), 401)
		print "Token's client ID does not match app's."
		response.headers['Content-Type'] = 'application/json'
		return response

	stored_access_token = login_session.get('access_token')
	stored_gplus_id = login_session.get('gplus_id')
	if stored_access_token is not None and gplus_id == stored_gplus_id:
		response = make_response(json.dumps('Current user is already connected.'),200)
		response.headers['Content-Type'] = 'application/json'
		return response

	# Store the access token in the session for later use.
	login_session['access_token'] = access_token
	login_session['gplus_id'] = gplus_id

	# Get user info
	userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
	params = {'access_token': credentials.access_token, 'alt': 'json'}
	answer = requests.get(userinfo_url, params=params)

	data = answer.json()

	login_session['username'] = data['name']
	login_session['picture'] = data['picture']
	login_session['email'] = data['email']

	#See if a user exists, if it doesn't make a new one
	user_id = getUserID(login_session['email'])
	if not user_id:
		user_id = createUser(login_session)
	login_session['user_id'] = user_id

	output = ''
	output += '<h1>Welcome, '
	output += login_session['username']
	output += '!</h1>'
	output += '<img src="'
	output += login_session['picture']
	output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
	flash("you are now logged in as %s" % login_session['username'])
	print "done!"
	print output
	return output


# User Helper Functions
# Create a user and return its id
def createUser(login_session):
	newUser = User(name=login_session['username'], email=login_session[
		'email'], picture=login_session['picture'])
	session.add(newUser)
	session.commit()
	user = session.query(User).filter_by(email=login_session['email']).one()
	return user.id


# Return a user by its user_id
def getUserInfo(user_id):
	user = session.query(User).filter_by(id=user_id).one()
	return user


# Return user_id by is email
def getUserID(email):
	try:
		user = session.query(User).filter_by(email=email).one()
		return user.id
	except:
		return None


# This function is called when sign out button is called
@app.route('/gdisconnect', methods=['POST'])
def gdisconnect():
	# Only disconnect a connected user.
	access_token = login_session.get('access_token')
	if access_token is None:
		response = make_response(json.dumps('Current user not connected.'), 401)
		response.headers['Content-Type'] = 'application/json'
		return response
	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]
	if result['status'] == '200':
		# Reset the user's sesson.
		del login_session['access_token']
		del login_session['gplus_id']
		del login_session['username']
		del login_session['email']
		del login_session['picture']

		response = make_response(json.dumps('Successfully disconnected.'), 200)
		response.headers['Content-Type'] = 'application/json'
		return response

	else:
		# For whatever reason, the given token was invalid.
		response = make_response(json.dumps('Failed to revoke token for given user.', 400))
		response.headers['Content-Type'] = 'application/json'
		return response


# Show render publichome.html when user has not logged in and render showitems.html when user has logged in
@app.route('/')
@app.route('/itemcatalog')
def itemHome():
	sports = session.query(Sports).all()
	equipment = session.query(Equipment).order_by(Equipment.id.desc())[0:6]
	if 'username' not in login_session:
		return render_template('publichome.html', sports=sports, equipment=equipment)
	else:
		return render_template('showitems.html', sports=sports, equipment=equipment)


# Click one sports will show equipmets in it
@app.route('/itemcatalog/<int:sports_id>')
def equipmentforonesports(sports_id):
	sports = session.query(Sports).all()
	catagory = session.query(Sports).filter_by(id = sports_id).one()
	equipment = session.query(Equipment).filter_by(sports_id=sports_id)
	if 'username' not in login_session:
		return render_template('publiconecatagory.html', sports=sports, equipment=equipment, catagory=catagory)
	else:
		return render_template('showonecatagory.html', sports=sports, catagory=catagory, equipment=equipment)


# Show details about one equipment
@app.route('/itemcatalog/<int:sports_id>/equipment/<int:equipment_id>')
def equipmentdetails(sports_id, equipment_id):
	sports = session.query(Sports).filter_by(id=sports_id).one()
	equipment = session.query(Equipment).filter_by(id=equipment_id).one()
	if 'username' not in login_session:
		return render_template('publiconeequipment.html', sports_id=sports_id, equipment_id=equipment_id, equipment=equipment, sports=sports)
	else:
		return render_template('showoneequipment.html', sports_id=sports_id, equipment_id=equipment_id, equipment=equipment, sports=sports)


# Enable clients to add new sports
@app.route('/itemcatalog/new', methods=["GET", "POST"])
def addsports():
	# If user has not logged in, redirect him to login.html 
	if 'username' not in login_session:
		return render_template("login.html")
	elif request.method == "GET":
		return render_template("addnewsports.html")
	else:
		newSports = Sports(name=request.form['newsports'], user_id=login_session['user_id'])
		session.add(newSports)
		session.commit()
		return redirect(url_for('itemHome'))


# Enable clients to add new equipments
@app.route('/itemcatalog/<int:sports_id>/new', methods=["GET", "POST"])
def addequipment(sports_id):
	sports = session.query(Sports).filter_by(id=sports_id)
	# If user has not logged in, redirect him to login.html 
	if 'username' not in login_session:
		return render_template("login.html")
	elif request.method == "GET":
		return render_template("addnewequipments.html", sports=sports)
	else:
		newEquipment = Equipment(sports_id=sports_id, name=request.form['newequipment'], description=request.form['description'], user_id=login_session['user_id'])
		session.add(newEquipment)
		session.commit()
		return redirect(url_for('itemHome'))


# Edit equipment in a sports
@app.route('/itemcatalog/<int:sports_id>/equipment/<int:equipment_id>/edit', methods=["GET","POST"])
def editequipment(sports_id, equipment_id):
	sports = session.query(Sports).all()
	# If user has not logged in, redirect him to login.html 
	if 'username' not in login_session:
		return redirect('/login')
	elif request.method == 'GET':
		return render_template('editequipment.html', sports=sports, sports_id=sports_id, equipment_id=equipment_id)
	else:
		# Check user id before do an add operation
		sports = session.query(Sports).filter_by(id=sports_id).one()
		if sports.user_id != login_session['user_id']:
			return "<script>function myFunction() {alert('You are not authorized to edit this sports. Please create your own sports in order to edit.');}</script><body onload='myFunction()''>"
		editedequipment = session.query(Equipment).filter_by(id=equipment_id).one()
		if request.form['editdescription']:
			editedequipment.description = request.form['editdescription']
		if request.form['editequipment']:
			editedequipment.name = request.form['editequipment']
		if request.form['catagories']:
			editedequipment.sports.name = request.form['catagories']
		session.add(editedequipment)
		session.commit()
		flash('Equipment Successfully Edited %s' % editedequipment.name)
		return redirect(url_for('itemHome'))


# Delete one equipment
@app.route('/itemcatalog/<int:equipment_id>/delete', methods=["GET", "POST"])
def deleteequipment(equipment_id):
	equipmentToDelete = session.query(Equipment).filter_by(id=equipment_id).one()
	# If user has not logged in, redirect him to login.html
	if 'username' not in login_session:
		return redirect('/login')
	# Check user id before do an add operation
	if equipmentToDelete.user_id != login_session['user_id']:
		return "<script>function myFunction() {alert('You are not authorized to delete this sports. Please create your own Sports in order to delete.');}</script><body onload='myFunction()''>"
	if request.method == 'POST':
		session.delete(equipmentToDelete)
		flash('%s Successfully Deleted' % equipmentToDelete.name)
		session.commit()
		return redirect(url_for('itemHome'))
	else:
		return render_template('deleteequipment.html', equipment=equipmentToDelete)


# An end point for returnning json files of a sports
@app.route('/itemcatalog/<int:sports_id>/equipment/JSON')
def sportsjason(sports_id):
	equipments = session.query(Equipment).filter_by(sports_id=sports_id)
	return jsonify(EquipmentItems=[i.serialize for i in equipments])

# An end point for returnning json files of all sports
@app.route('/itemcatalog/JSON')
def equipmentjason():
	sports = session.query(Sports).all()
	return jsonify(SportsItems=[i.serialize for i in sports])


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)