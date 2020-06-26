from src import parsesnakeobj, parseopponents, parsefood, initboard, start, move, end
from src.utils.constants import EMPTY

def test_parsesnakeobj():
    snake = {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
          {"x": 0, "y": 0}, 
          {"x": 1, "y": 0}, 
          {"x": 2, "y": 0}
        ],
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??"
    }
    index = 3
    gameboard = [[EMPTY] * 5 for i in range(5)]
    parsedsnake = parsesnakeobj(snake, index, gameboard)
    assert parsedsnake['id'] == snake['id']
    assert parsedsnake['hp'] == snake['health']
    assert parsedsnake['length'] == snake['length']