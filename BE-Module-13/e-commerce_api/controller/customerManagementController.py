from flask import jsonify, request
from service.customerManagementService import login_customer


def login():
    customer = request.json

    if not customer.get('username') or not customer.get('password'):
        return jsonify({'message': 'Username and password are required'}), 400

    user = login_customer(customer['username'], customer['password'])
    
    if user:
        return user, 200
    else:
        resp ={
                "status":"Error",
                "message":"Incorrect credencials"
            }
        return jsonify(resp), 404
