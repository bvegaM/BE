from flask import jsonify
from models.customerManagement import CustomerManagement
from database import db
from utils.util import encode_token

def login_customer(username, password):
    user = CustomerManagement.query.filter(CustomerManagement.username == username, CustomerManagement.password == password).one_or_none()
    print(user)
    if user:
        auth_token = encode_token(user.id)
        resp = {

            "status":"succes",
            "message" :"Successfully logged in",
            'auth_token':auth_token
        }
        return jsonify(resp)
    else:
        return None
