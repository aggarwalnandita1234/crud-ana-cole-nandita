from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key="group_project"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index1():
	query= "SELECT * FROM users"
	users=mysql.query_db(query)
	# print users
	return render_template('index.html', all_users=users)

@app.route('/create')
def create():
	return render_template('create.html')

@app.route('/add', methods=['POST'])
def add():
	# name= request.form['name']
	# occupation= request.form['occupation']
	# print name, occupation
	query="INSERT INTO users(name, occupation) VALUES (:name, :occupation);"
	data={
		'name': request.form['name'],
		'occupation': request.form['occupation']
	}
	users=mysql.query_db(query, data)
	return redirect('/')

@app.route('/show/<user_id>')
def show(user_id):
	
	print user_id
	query="SELECT * FROM users WHERE idusers=:user_id"
	data={'user_id': user_id }
	
	user=mysql.query_db(query, data)

	return render_template('display.html', user=user)

@app.route('/edit/<user_id>')
def edit(user_id):

	print user_id
	query="SELECT * FROM users WHERE idusers=:user_id"
	data={'user_id': user_id }
	
	user=mysql.query_db(query, data)

	return render_template('edit.html', user=user)

@app.route('/update', methods=['POST'])
def update():

	user_id=request.form['id']
	print user_id
	new_name=request.form['name']
	print new_name
	new_occupation=request.form['occupation']
	print new_occupation
	query="UPDATE users SET name=:new_name, occupation=:new_occupation WHERE idusers=:user_id"
	data={'user_id': user_id,
		  'new_name': new_name,
		  'new_occupation': new_occupation}
	print data
	user=mysql.query_db(query, data)
	return redirect('/')

@app.route('/delete')
def delete():


	flash("Are you sure?")
	return redirect('/')

@app.route('/delete_yes', methods=['POST'])
def delete_yes():
	user_id=request.form['id']
	print user_id
	query="DELETE FROM users WHERE idusers=:user_id"
	data={'user_id': user_id}
	mysql.query_db(query, data)
	return redirect('/')

@app.route('/delete_no')
def delete_no():
	return redirect('/')





app.run(debug=True)