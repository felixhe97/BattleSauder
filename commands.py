import myredis
import db

import utils

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