from typing import List, Dict, Union

# types from request object
Board = List[List[int]]
Coordinates = Dict[str, int]
Snake = Dict[str, Union[str, int, Coordinates]]

# response types
BattleSnakeResponse = Dict[str, str]