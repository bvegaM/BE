import hashlib
import time

# Step 1: Create an empty dictionary to store user credentials
user_credentials = {}

# Step 2: Register a new user
def register_user(username, password):
    start_time = time.time()  # Start time for registration
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_credentials[username] = hashed_password
    end_time = time.time()  # End time for registration
    registration_time = end_time - start_time
    print(f"User '{username}' registered successfully in {registration_time:.7f} seconds!")

# Step 3: Login user
def login_user(username, password):
    start_time = time.time()  # Start time for login
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stored_password = user_credentials.get(username)
    if stored_password and stored_password == hashed_password:
        end_time = time.time()  # End time for login
        login_time = end_time - start_time
        print(f"Welcome back, {username}! Logged in successfully in {login_time:.7f} seconds.")
    else:
        print("Invalid username or password.")

# Test the implementation
register_user('user1', 'password123')
login_user('user1', 'password123')