import astar
import printer

# constants for index of people
EMPTY = 0
FOOD = 1
# you are 2, opponents are 3 - 9
INDEXSTART = 2

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

def moveup():
    return {'move': 'up', 'shout': 'gangg'}

def moveleft():
    return {'move': 'left', 'shout': 'ganggangg'}

def moveright():
    return {'move': 'right', 'shout': 'swerve'}

def movedown():
    return {'move': 'down', 'shout': 'skrrrt'}

def nextmove(board, food, snakes):
    # TODO
    return