# constants for index of people
EMPTY = 0
NOTEMPTY = '.'
FOOD = 1
# you are 2, opponents are 3 - 9
INDEXSTART = 2

# from x y graphics to x y cartesian
def moveup() -> dict:
    print('moveup - bs move left')
    return {'move': 'left', 'shout': 'gangg'}

def movedown() -> dict:
    print('movedown - bs move right')
    return {'move': 'right', 'shout': 'skrrrt'}

def moveleft() -> dict:
    print('moveleft - bs move down')
    return {'move': 'down', 'shout': 'ganggangg'}

def moveright() -> dict:
    print('moveright - bs move up')
    return {'move': 'up', 'shout': 'swerve'}