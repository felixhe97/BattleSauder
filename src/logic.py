from queue import SimpleQueue
from typing import Callable
from .utils import FOOD, INDEXSTART, EMPTY, NOTEMPTY, moveup, movedown, moveleft, moveright
from .printer import printbattlesnakeboard, printboard, printfood, printsnakes
import random

def bfsfood(board: list, startingx: int, startingy: int) -> list:
    # instantiation of queue with type annotation for mypy
    q: SimpleQueue = SimpleQueue()
    q.put((startingx, startingy))
    nearestfoodarr = []
    bfslevel = 0
    while not q.empty():
        tempsize = q.qsize()
        while tempsize > 0:
            coord = q.get()
            x = coord[0]
            y = coord[1]
            # mark on gameboard that we visited empty space
            if board[x][y] == EMPTY:
                board[x][y] = NOTEMPTY
            if board[x][y] == FOOD:
                # also have travel distance as third element
                nearestfoodarr.append((x, y, bfslevel))
            if x > 0 and board[x-1][y] == EMPTY:
                q.put((x-1, y))
            if x < len(board) - 1 and board[x+1][y] == EMPTY:
                q.put((x+1, y))
            if y > 0 and board[x][y-1] == EMPTY:
                q.put((x, y-1))
            if y < len(board[0]) - 1 and board[x][y+1] == EMPTY:
                q.put((x, y+1))
            tempsize = tempsize - 1
        bfslevel = bfslevel + 1
    return nearestfoodarr

def directiontofood(canmove: list, myx: int, myy: int, foodx: int, foody: int):
    # TODO
    return []

def createavailablemoves(board, myx, myy):
    validmove = []
    if myx > 0 and board[myx-1][myy] == EMPTY:
        validmove.append(moveup)
    if myx < len(board) - 1 and board[myx+1][myy] == EMPTY:
        validmove.append(movedown)
    if myy > 0 and board[myx][myy-1] == EMPTY:
        validmove.append(moveleft)
    if myy < len(board[0]) - 1 and board[myx][myy+1] == EMPTY:
        validmove.append(moveright)
    return validmove

def nextmove(board: list, food: list, snakes: list) -> Callable[[], dict]:
    mysnake = snakes[INDEXSTART]
    myx = mysnake['head'][0]
    myy = mysnake['head'][1]
    canmove = createavailablemoves(board, myx, myy)
    if canmove.count == 0:
        print('no valid moves')
        return moveright
    else:
        if mysnake['hp'] < (len(board) * 2):
            nearestfood = bfsfood(board, myx, myy)
            foodx = nearestfood[0]
            foody = nearestfood[1]
            tofood = directiontofood(canmove, myx, myy, foodx, foody)
            return random.choice(tofood)
        else:
            return random.choice(canmove)