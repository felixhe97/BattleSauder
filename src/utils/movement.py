from src.utils.saudertyping import BattleSnakeResponse

# from x y graphics to x y cartesian
def move_up() -> BattleSnakeResponse:
    print('moveup - bs move left')
    return {'move': 'left', 'shout': 'gangg'}

def move_down() -> BattleSnakeResponse:
    print('movedown - bs move right')
    return {'move': 'right', 'shout': 'skrrrt'}

def move_left() -> BattleSnakeResponse:
    print('moveleft - bs move down')
    return {'move': 'down', 'shout': 'ganggangg'}

def move_right() -> BattleSnakeResponse:
    print('moveright - bs move up')
    return {'move': 'up', 'shout': 'swerve'}