from typing import Dict

# from x y graphics to x y cartesian
def moveup() -> Dict:
    print('moveup - bs move left')
    return {'move': 'left', 'shout': 'gangg'}

def movedown() -> Dict:
    print('movedown - bs move right')
    return {'move': 'right', 'shout': 'skrrrt'}

def moveleft() -> Dict:
    print('moveleft - bs move down')
    return {'move': 'down', 'shout': 'ganggangg'}

def moveright() -> Dict:
    print('moveright - bs move up')
    return {'move': 'up', 'shout': 'swerve'}