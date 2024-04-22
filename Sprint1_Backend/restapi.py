import flask
from flask import jsonify
from flask import request

from sql import create_connection
from sql import execute_read_query
from sql import execute_query

import mysql.connector
from mysql.connector import Error
import creds


#setting up an application name
app = flask.Flask(__name__)
app.config["DEBUG"] = True #allow to show errors in browser


# Creates the Login API with preset 'username' and 'password'
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    if username == 'myusername' and password == 'mypassword':
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'})

# Create a new cargo record
@app.route('/cargo', methods=['POST'])
def add_cargo():
    weight = request.json['weight']
    cargotype = request.json['cargotype']
    shipid = request.json['shipid']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO cargo (weight, cargotype, shipid) VALUES (%s, %s, %s)", (weight, cargotype, shipid))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Cargo added successfully'})



# Retrieve all cargo records
@app.route('/cargo', methods=['GET'])
def get_all_cargo():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cargo")
    cargo = cur.fetchall()
    cur.close()
    return jsonify({'cargo': cargo})

# Retrieve a specific cargo record by ID
@app.route('/cargo/<int:id>', methods=['GET'])
def get_cargo_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cargo WHERE id = %s", (id,))
    cargo = cur.fetchone()
    cur.close()
    return jsonify({'cargo': cargo})

# Update a specific cargo record by ID
@app.route('/cargo/<int:id>', methods=['PUT'])
def update_cargo(id):
    weight = request.json['weight']
    cargotype = request.json['cargotype']
    shipid = request.json['shipid']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE cargo SET weight = %s, cargotype = %s, shipid = %s WHERE id = %s", (weight, cargotype, shipid, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Cargo updated successfully'})

# Delete a specific cargo record by ID
@app.route('/cargo/<int:id>', methods=['DELETE'])
def delete_cargo(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cargo WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'Cargo deleted successfully'})

################### ALL CODE ABOVE IS USED FOR CARGO TABLE ###################

app.run()
