from src.utils.saudertyping import BattleSnakeResponse

# from x y graphics to x y cartesian
def moveup() -> BattleSnakeResponse:
    print('moveup - bs move left')
    return {'move': 'left', 'shout': 'gangg'}

def movedown() -> BattleSnakeResponse:
    print('movedown - bs move right')
    return {'move': 'right', 'shout': 'skrrrt'}

def moveleft() -> BattleSnakeResponse:
    print('moveleft - bs move down')
    return {'move': 'down', 'shout': 'ganggangg'}

def moveright() -> BattleSnakeResponse:
    print('moveright - bs move up')
    return {'move': 'up', 'shout': 'swerve'}