from .utils import EMPTY, FOOD, INDEXSTART
from .logic import nextmove
from typing import Union

def createsnakeobj(snake: dict, index: int, graph: list) -> dict:
    coordarr = []
    for coord in snake['body']:
        x = coord['x']
        y = coord['y']
        coordarr.append((x, y))
        graph[x][y] = index
    snakeObj = {
            'id': snake['id'],
            'hp': snake['health'],
            'body': coordarr,
            'head': (snake['head']['x'], snake['head']['y']),
            'length': snake['length']
            }
    return snakeObj

def initboard(width: int, height: int, foodarr: list, opponents: list) -> dict:
    # switch it to graphics x y
    matrix = [[EMPTY] * height for i in range(width)]
    tempfood = []
    for food in foodarr:
        matrix[food['x']][food['y']] = FOOD
        tempfood.append((food['x'],food['y']))
    index = INDEXSTART
    snakearr = [[] for i in range(index)]
    for snake in opponents:
        snakearr.append(createsnakeobj(snake, index, matrix))
        index = index + 1
    return {'board': matrix, 'food': tempfood, 'snakes': snakearr}

def end(jsonobj: dict) -> str:
    return ''

def startmove(jsonobj: dict) -> Union[dict, str]:
    if 'you' in jsonobj:
        ds = initboard(jsonobj['board']['width'], jsonobj['board']['height'],
            jsonobj['board']['food'], jsonobj['board']['snakes'])
        return nextmove(ds['board'], ds['food'], ds['snakes'])()
    else:
        return ''