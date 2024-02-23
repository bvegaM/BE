from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTcwODYxMjI2MCwiaWF0IjoxNzA4NjEyMjYwfQ.cdDAftOQ5kp9PEOLSuVlrmqhkD4zFF5lbvBX3ysNJI8'

def encode_token(user_id, role_names):
    payload ={
        'exp': datetime.utcnow() + timedelta(days=0, hours=1),
        'iat' :datetime.utcnow(),
        'sub':user_id,
        'roles': role_names
        
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm= 'HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            print(request.headers)
            token = request.headers["Authorization"].split(" ")[1]

            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401
            

            expire = payload['exp']
            if expire < datetime.utcnow():
                return {
                    "message": "Token has expired",
                    "error": "Unauthorized"
                }, 401

        if not token:
            return {
                "message": "Authentication Token is missing",
                "error": "Unauthorized"
            }, 401

        return f(token, *args, **kwargs)

    return decorated

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]
            if not token:
                return jsonify({'message': 'Token is missing'}), 401

            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401

            roles = payload["roles"]
            

            if role not in roles:
                return jsonify({'message': 'User does not have the required role'}), 403

            return f(*args, **kwargs)

        return decorated_function

    return decorator