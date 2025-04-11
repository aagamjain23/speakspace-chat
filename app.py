from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key'  # required by SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)  # Sends to everyone

if __name__ == '__main__':
    socketio.run(app, debug=True)
