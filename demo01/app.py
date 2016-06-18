###################################
#         Data thread
###################################
from threading import Thread, Event
import time, random

thread = Thread()
thread_stop_event = Event()
LINES = open('data.txt').read().splitlines()
messages_list = []

class DataThread(Thread):
    def run(self):
        while not thread_stop_event.isSet():
            item = random.choice(LINES)
            print "Message: ", item
            messages_list.append(unicode(item, "utf-8"))
            time.sleep(random.randint(1,3))


            
###################################
#      Flask application
###################################
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', messages=reversed(messages_list))
                    
if __name__ == '__main__':
    if not thread.isAlive():
        thread = DataThread()
        thread.start()

    app.run(debug=True, port=5001)
    thread_stop_event.set()
    
