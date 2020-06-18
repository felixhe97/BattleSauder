from flask import Flask, request
app = Flask(__name__)

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
    return commands.start(request.json)

@app.route("/move", methods=["POST"])
def move_snake():
    return commands.move(request.json)

@app.route("/end", methods=["POST"])
def end_game():
    return commands.end(request.json)