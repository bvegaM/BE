from flask import jsonify
from models.customerManagement import CustomerManagement
from database import db
from utils.util import encode_token
from werkzeug.security import check_password_hash

def login_customer(username, password):
    user = CustomerManagement.query.filter(CustomerManagement.username == username).one_or_none()
    role_names = [role.role_name for role in user.roles]
    if user:
        if check_password_hash(user.password, password):
            auth_token = encode_token(user.id,role_names)
            resp = {

                "status":"succes",
                "message" :"Successfully logged in",
                'auth_token':auth_token
            }
            return jsonify(resp)
        else:
            return None
    else:
        return None
