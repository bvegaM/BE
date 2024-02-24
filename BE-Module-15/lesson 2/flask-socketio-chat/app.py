#!/bin/env python
import json
from flask import render_template
from web_socket_server import WebSocketServer, socketio, app

app = WebSocketServer().create_app()
user_messages = {}

@socketio.on('message')
def handle_message(message):
    message = json.loads(message)
    print(f'Received message: {message}')
    username = message['user']
    msg = message['message']
    
    if username in user_messages:
        user_messages[username].append(msg)
    else:
        user_messages[username] = [msg]
    
    socketio.emit('message', message['user']+" "+message['message'])


@socketio.on('get_all_messages')
def handle_get_user_messages():
    socketio.emit('get_user_messages', messages)


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)