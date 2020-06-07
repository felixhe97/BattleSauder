from flask import Flask, request
app = Flask(__name__)

#TODO HEROKU redis and psql?

@app.route("/")
def battlesnake_info():
    return {
        "apiversion": "0.1",
        "author": "felixhe97"
    }

@app.route("/start", methods=["POST"])
def init_game():
    reqBody = request.json
    print(request)
    return ""

@app.route("/move", methods=["POST"])
def move_snake():
    reqBody = request.json
    print(reqBody["game"])
    return {
        "move": "up",
        "shout": "moving up I guess"
    }

@app.route("/end", methods=["POST"])
def end_game():
    reqBody = request.json
    print(request)
    return ""