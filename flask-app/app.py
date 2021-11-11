from flask import Flask, render_template
import os

app = Flask(__name__)

images = os.listdir('./static/')
cache = {'idx': 0}

@app.route("/")
def oreo():
    img_name = images[cache['idx'] % len(images)]
    increment()
    return render_template('index.html', img_name=img_name)

def increment():
    cache['idx'] = cache['idx'] + 1
    return 'Incremented cache!'
