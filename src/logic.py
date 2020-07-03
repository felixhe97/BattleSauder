from collections import deque
from typing import Callable
from .utils.constants import FOOD, INDEXSTART, EMPTY, NOTEMPTY
from .utils.movement import moveup, movedown, moveleft, moveright
from .utils.printer import printbattlesnakeboard, printboard, printfood, printsnakes
from typing import List, Dict
from .utils.saudertyping import Board
import random

def bfsfood(board: Board, startingx: int, startingy: int) -> List:
    q: deque = deque()
    q.append((startingx, startingy))
    nearestfoodarr = []
    bfslevel = 0
    while len(q) != 0:
        tempsize = len(q)
        while tempsize > 0:
            coord = q.popleft()
            x = coord[0]
            y = coord[1]
            # mark on gameboard that we visited empty space
            if board[x][y] == EMPTY:
                board[x][y] = NOTEMPTY
            if board[x][y] == FOOD:
                # also have travel distance as third element
                nearestfoodarr.append((x, y, bfslevel))
            if x > 0 and board[x-1][y] == EMPTY:
                q.append((x-1, y))
            if x < len(board) - 1 and board[x+1][y] == EMPTY:
                q.append((x+1, y))
            if y > 0 and board[x][y-1] == EMPTY:
                q.append((x, y-1))
            if y < len(board[0]) - 1 and board[x][y+1] == EMPTY:
                q.append((x, y+1))
            tempsize -= 1
        bfslevel += 1
    return nearestfoodarr

def directiontofood(canmove: list, myx: int, myy: int, foodx: int, foody: int) -> List:
    tofood = []
    if foodx > myx and movedown in canmove:
        tofood.append(movedown)
    elif foodx < myx and moveup in canmove:
        tofood.append(moveup)
    if foody > myy and moveright in canmove:
        tofood.append(moveright)
    elif foody < myy and moveleft in canmove:
        tofood.append(moveleft)
    return tofood

def createavailablemoves(board: Board, myx: int, myy: int) -> List:
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

def nextmove(board: Board, food: list, snakes: List) -> Callable[[], dict]:
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
            print('called tofood')
            print(tofood)
            return random.choice(tofood)
        else:
            print('called canmove')
            print(canmove)
            printbattlesnakeboard(board)
            printsnakes(snakes)
            printfood(food)
            return random.choice(canmove)