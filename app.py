import os
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()
    if data:
        socketio.emit('new_alert', data)
        return {"message": "Data received and alert sent!"}, 200
    return {"message": "No data received!"}, 400

@app.route('/')
def index():
    return render_template("index_x.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000 for local testing
    socketio.run(app, debug=True, host="0.0.0.0", port=port)
