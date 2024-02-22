from datetime import datetime, timedelta
from functools import wraps
from flask import request
import jwt

SECRET_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTcwODYxMjI2MCwiaWF0IjoxNzA4NjEyMjYwfQ.cdDAftOQ5kp9PEOLSuVlrmqhkD4zFF5lbvBX3ysNJI8'

def encode_token(user_id):
    payload ={
        'exp': datetime.utcnow() + timedelta(days=0, hours=1),
        'iat' :datetime.utcnow(),
        'sub':user_id
        
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm= 'HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
            print(token)
        if not token:
            return {
                "message": "Authentication Token is missing",
                "error": "Unauthorized"
            }, 401

        return f(token, *args, **kwargs)

    return decorated