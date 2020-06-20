from .utils import EMPTY, FOOD, INDEXSTART
from .logic import nextmove
from typing import Union

def createsnakeobj(snake: dict, index: int, graph: list) -> dict:
    coordarr = []
    for coord in snake['body']:
        coordarr.append([coord['x'], coord['y']])
        graph[coord['x']][coord['y']] = index
    snakeObj = {
            'id': snake['id'],
            'hp': snake['health'],
            'body': coordarr,
            'head': [snake['head']['x'], snake['head']['y']],
            'length': snake['length']
            }
    return snakeObj

def initboard(mi: int, mj: int, foodarr: list, opponents: list) -> dict:
    matrix = [[EMPTY] * mi for i in range(mj)]
    tempfood = []
    for food in foodarr:
        matrix[food['x']][food['y']] = FOOD
        tempfood.append([food['x'],food['y']])
    snakemap = {}
    index = INDEXSTART
    for snake in opponents:
        snakemap[index] = createsnakeobj(snake, index, matrix)
        index = index + 1
    return {'board': matrix, 'food': tempfood, 'snakes': snakemap}

def end(jsonobj: dict) -> str:
    return ''

def start(jsonobj: dict) -> Union[dict, str]:
    if 'you' in jsonobj:
        # start game with you in it
        ds = initboard(jsonobj['board']['width'], jsonobj['board']['height'],
            jsonobj['board']['food'], jsonobj['board']['snakes'])
        # inmem[jsonobj['game']['id']] = ds
        return nextmove(ds['board'], ds['food'], ds['snakes'])()
    else:
        return ''

def move(jsonobj: dict) -> Union[dict, str]:
    return start(jsonobj)