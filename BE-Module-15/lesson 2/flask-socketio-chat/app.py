#!/bin/env python
from flask import render_template
from web_socket_server import WebSocketServer, socketio, app

app = WebSocketServer().create_app()
messages = []

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    messages.append(message)
    socketio.emit('message', message)

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