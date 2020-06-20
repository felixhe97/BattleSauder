# constants for index of people
EMPTY = 0
FOOD = 1
# you are 2, opponents are 3 - 9
INDEXSTART = 2

# from x y graphics to x y cartesian
def moveup() -> dict:
    return {'move': 'up', 'shout': 'gangg'}

def movedown() -> dict:
    return {'move': 'down', 'shout': 'skrrrt'}

def moveleft() -> dict:
    return {'move': 'left', 'shout': 'ganggangg'}

def moveright() -> dict:
    return {'move': 'right', 'shout': 'swerve'}