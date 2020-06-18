# from .myredis import r
# from .db import conn

from .utils import EMPTY, FOOD, INDEXSTART

def createsnakeobj(snake, index, graph):
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

def initboard(mi, mj, foodarr, opponents, mysnake):
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

def merge(prevstate, newinfo):
    # TODO
    return

def nextmove(board, food, snakes):
    # TODO
    return

inmem = {}

def end(jsonobj):
    # todo store info, win/lose
    gameid = jsonobj['game']['id']
    if gameid in inmem:
        inmem.pop(gameid)
    return

def move(jsonobj):
    gameid = jsonobj['game']['id']
    if 'you' in jsonobj and gameid in inmem:
        merge(inmem[gameid], jsonobj)
        return nextmove(inmem[gameid]['board'], inmem[gameid]['food'],
                inmem[gameid]['snakes'])
    else:
        # not in game
        return

def start(jsonobj):
    if 'you' in jsonobj:
        # start game with you in it
        ds = initboard(jsonobj['board']['width'], jsonobj['board']['height'],
            jsonobj['board']['food'], jsonobj['board']['snakes'],
            jsonobj['you'])
        inmem[jsonobj['game']['id']] = ds
        return nextmove(ds['board'], ds['food'], ds['snakes'])
    else:
        return