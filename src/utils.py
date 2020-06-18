# constants for index of people
EMPTY = 0
FOOD = 1
# you are 2, opponents are 3 - 9
INDEXSTART = 2

def printboard(board):
    for row in board:
        print(row)

def printsnakes(snakes):
    for i, snake in snakes.items():
        print(i, snake)

def printfood(food):
    for x in food:
        print(x)

def moveup():
    return {'move': 'up', 'shout': 'gangg'}

def moveleft():
    return {'move': 'left', 'shout': 'ganggangg'}

def moveright():
    return {'move': 'right', 'shout': 'swerve'}

def movedown():
    return {'move': 'down', 'shout': 'skrrrt'}