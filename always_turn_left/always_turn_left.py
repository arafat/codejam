"""Programs to implement Always Turn Left problem from Google Code Jam.

Problem Url: https://code.google.com/codejam/contest/32003/dashboard#s=p1
"""

from utils import utils
import config

_INPUT_FILE_PATH = 'always_turn_left/test_data/always_turn_left.in'
_WALK = 'W'
_RIGHT = 'R'
_LEFT = 'L'

_NORTH = 'NORTH'
_SOUTH = 'SOUTH'
_EAST = 'EAST'
_WEST = 'WEST'

_DIRECTION_MAP = {
    (_NORTH, 'L'): _WEST,
    (_NORTH, 'R'): _EAST,
    (_SOUTH, 'L'): _EAST,
    (_SOUTH, 'R'): _WEST,
    (_EAST, 'L'): _NORTH,
    (_EAST, 'R'): _SOUTH,
    (_WEST, 'L'): _SOUTH,
    (_WEST, 'R'): _NORTH
}

_ROOM_CONFIG_INDEX_MAP = {
    _NORTH: 0,
    _SOUTH: 1,
    _WEST: 2,
    _EAST: 3
}

_DIRECTION_FLIP_MAP = {
    _NORTH: _SOUTH,
    _SOUTH: _NORTH,
    _WEST: _EAST,
    _EAST: _WEST
}


def GetNewDirection(current_direction, move):
  return _DIRECTION_MAP[(current_direction, move)]


def GetWallIndex(direction, entering=True):
  if entering:
    direction = _DIRECTION_FLIP_MAP[direction]
  return _ROOM_CONFIG_INDEX_MAP[direction]


def UpdateMazeConfiguration(maze, step, row, col, current_direction):
  if step == _WALK:
    maze[(row, col)][GetWallIndex(current_direction, False)] = 1
    if current_direction == 'SOUTH':
      row -= 1
    elif current_direction == 'NORTH':
      row += 1
    elif current_direction == 'WEST':
      col -= 1
    elif current_direction == 'EAST':
      col += 1
    if not (row, col) in maze:
      maze[(row, col)] = [0, 0, 0, 0]
      maze[(row, col)][GetWallIndex(current_direction)] = 1
      print 'Its a walk command.'
  else:
    current_direction = GetNewDirection(current_direction, step)
  return maze, row, col, current_direction


def GetMazeDefination(path, return_path):
  direction = 'SOUTH'
  row = 0; col = 0
  # ['N', 'S', 'W', 'E']
  maze = {(row, col): [1, 0, 0, 0]}
  for step in path[1:-1]:
    maze, row, col, direction = UpdateMazeConfiguration(
        maze, step, row, col, direction)
  direction = _DIRECTION_FLIP_MAP[direction]
  maze[(row, col)] = [0, 0, 0, 0]
  maze[(row, col)][GetWallIndex(direction)] = 1
  for step in return_path[1:-1]:
    maze, row, col, direction = UpdateMazeConfiguration(
        maze, step, row, col, direction)
  return maze


def Run():
  in_iter = utils.GetInputData(_INPUT_FILE_PATH, 1, 1)
  for input in in_iter:
    path, return_path = input[0][0].split(' ')
    print GetMazeDefination(path, return_path)
    break
