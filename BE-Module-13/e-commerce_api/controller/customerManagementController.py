
from flask import jsonify, request
from service.customerManagementService import login_customer

def login():
    customer = request.json
    user = login_customer(customer['username'], customer['password'])
    if user:
        return user, 200
    else:
        resp ={
                "status":"Error",
                "message":"User does not exist"
            }
        return jsonify(resp), 404
    