from .utils import EMPTY, FOOD, INDEXSTART
from .logic import nextmove
from typing import Union

def parsesnakeobj(snake: dict, index: int, gameboard: list) -> dict:
    # marks gameboard while parsing snake body
    coordarr = []
    for coord in snake['body']:
        x = coord['x']
        y = coord['y']
        coordarr.append((x, y))
        gameboard[x][y] = index
    snakeObj = {
            'id': snake['id'],
            'hp': snake['health'],
            'body': coordarr,
            'head': (snake['head']['x'], snake['head']['y']),
            'length': snake['length']
            }
    return snakeObj

def parsefood(matrix, foodarr):
    tempfood = []
    for food in foodarr:
        matrix[food['x']][food['y']] = FOOD
        tempfood.append((food['x'],food['y']))
    return tempfood

def parseopponents(matrix, index, opponents):
    # fills snakearr with empty arrays so that to iterate over
    # all snakes, use 'for i in range(INDEXSTART, len(snakearr))'
    snakearr = [[] for i in range(index)]
    for snake in opponents:
        snakearr.append(parsesnakeobj(snake, index, matrix))
        index = index + 1
    return snakearr

def initboard(width: int, height: int, foodarr: list, opponents: list) -> dict:
    # switch it to graphics x y
    gameboard = [[EMPTY] * height for i in range(width)]
    tempfood = parsefood(gameboard, foodarr)
    snakearr = parseopponents(gameboard, INDEXSTART, opponents)
    return {'board': gameboard, 'food': tempfood, 'snakes': snakearr}

def end(jsonobj: dict) -> str:
    return ''

def start(jsonobj: dict) -> Union[dict, str]:
    if 'you' in jsonobj:
        ds = initboard(jsonobj['board']['width'], jsonobj['board']['height'],
            jsonobj['board']['food'], jsonobj['board']['snakes'])
        return nextmove(ds['board'], ds['food'], ds['snakes'])()
    else:
        return ''

def move(jsonobj: dict) -> Union[dict, str]:
    return start(jsonobj)