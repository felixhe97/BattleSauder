from flask import Flask, request
app = Flask(__name__)

from src import startmove, end

@app.route("/")
def battlesnake_info():
    return {
        "apiversion": "1",
        "author": "felixhe97",
        "color": "#BADBAD",
        "head": "pixel",
        "tail": "pixel"
    }

@app.route("/start", methods=["POST"])
def init_game():
    return startmove(request.json)

@app.route("/move", methods=["POST"])
def move_snake():
    return startmove(request.json)

@app.route("/end", methods=["POST"])
def end_game():
    return end(request.json)