###################################
#         Data thread
###################################
from threading import Thread, Event
import time, random, json

thread = Thread()
thread_stop_event = Event()
LINES = open('data.txt').read().splitlines()
            
class DataThread(Thread):
    def run(self):
        while not thread_stop_event.isSet():
            item = random.choice(LINES)
            print "Message: ", item
            socketio.emit('update', json.dumps({"message": item}) , namespace='/test')
            time.sleep(random.randint(2,5))

            
###################################
#      Flask application
###################################
from flask import Flask, render_template, request
from flask.ext.socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def on_test_connect():
    print " # Client connected: ", request.remote_addr
    
    global thread
    if not thread.isAlive():
        thread = DataThread()
        thread.start()
                        
    socketio.emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def on_test_disconnect():
    print " # Client disconnected: ", request.remote_addr

                    
if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, debug=True, port=5002)
