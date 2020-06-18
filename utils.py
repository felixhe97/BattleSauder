import snakeutils
import examplejson

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
    matrix = [[snakeutils.EMPTY] * mi for i in range(mj)]
    tempfood = []
    for food in foodarr:
        matrix[food['x']][food['y']] = snakeutils.FOOD
        tempfood.append([food['x'],food['y']])
    snakemap = {}
    index = snakeutils.INDEXSTART
    for snake in opponents:
        snakemap[index] = createsnakeobj(snake, index, matrix)
        index = index + 1
    return {'board': matrix, 'food': tempfood, 'snakes': snakemap}

def merge(prevstate, newinfo):
    return

def nextmove(board, food, snakes):
    return

# TODO
redis = {}

def end(jsonobj):
    # todo store info, win/lose
    gameid = jsonobj['game']['id']
    if gameid in redis:
        redis.pop(gameid)
    return

def move(jsonobj):
    gameid = jsonobj['game']['id']
    if 'you' in jsonobj and gameid in redis:
        merge(redis[gameid], jsonobj)
        return nextmove(redis[gameid]['board'], redis[gameid]['food'],
                redis[gameid]['snakes'])
    else:
        # not in game
        return

def start(jsonobj):
    if 'you' in jsonobj:
        # start game with you in it
        ds = initboard(jsonobj['board']['width'], jsonobj['board']['height'],
            jsonobj['board']['food'], jsonobj['board']['snakes'],
            jsonobj['you'])
        redis[jsonobj['game']['id']] = ds
        return nextmove(ds['board'], ds['food'], ds['snakes'])
    else:
        return

temp = start(examplejson.json1)
snakeutils.printboard(temp['board'])
snakeutils.printsnakes(temp['snakes'])
snakeutils.printfood(temp['food'])

temp = move(examplejson.json2)
snakeutils.printboard(temp['board'])
snakeutils.printsnakes(temp['snakes'])
snakeutils.printfood(temp['food'])
