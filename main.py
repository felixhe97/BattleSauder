from flask import Flask, request
app = Flask(__name__)

import src

@app.route("/")
def battlesnake_info():
    return {
        "apiversion": "0.1",
        "author": "felixhe97",
        "color": "#FFFFFF",
        "head": "pixel",
        "tail": "pixel"
    }

@app.route("/start", methods=["POST"])
def init_game():
    return src.start(request.json)

@app.route("/move", methods=["POST"])
def move_snake():
    return src.move(request.json)

@app.route("/end", methods=["POST"])
def end_game():
    return src.end(request.json)