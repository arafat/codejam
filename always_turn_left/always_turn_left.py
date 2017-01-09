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


def GetMazeDefination(path, return_path):
  direction = 'SOUTH'
  row = 0; col = 0
  # ['N', 'S', 'W', 'E']
  grid = {(0, 0): [1, 0, 0, 0]}
#  new_path = path[1:-1] + 'RR' + return_path[1:-1]
  for cmd in path[1:-1]:
    if cmd == _WALK:
      grid[(row, col)][GetWallIndex(direction, False)] = 1
      if direction == 'SOUTH':
        row -= 1
      elif direction == 'NORTH':
        row += 1
      elif direction == 'WEST':
        col -= 1
      elif direction == 'EAST':
        col += 1
      if not (row, col) in grid:
        grid[(row, col)] = [0, 0, 0, 0]
      grid[(row, col)][GetWallIndex(direction)] = 1
      print 'Its a walk command.'
    else:
      direction = GetNewDirection(direction, cmd)
  direction = _DIRECTION_FLIP_MAP[direction]
  room = [0, 0, 0, 0]
  room[GetWallIndex(direction)] = 1
  grid[(row, col)] = room
  for cmd in return_path[1:-1]:
    if cmd == _WALK:
      grid[(row, col)][GetWallIndex(direction, False)] = 1
      if direction == 'SOUTH':
        row -= 1
      elif direction == 'NORTH':
        row += 1
      elif direction == 'WEST':
        col -= 1
      elif direction == 'EAST':
        col += 1
      if not (row, col) in grid:
        grid[(row, col)] = [0, 0, 0, 0]
      grid[(row, col)][GetWallIndex(direction)] = 1
      print 'Its a walk command.'
    else:
      direction = GetNewDirection(direction, cmd)
  return grid


def Run():
  in_iter = utils.GetInputData(_INPUT_FILE_PATH, 1, 1)
  for input in in_iter:
    path, return_path = input[0][0].split(' ')
    print GetMazeDefination(path, return_path)
    break
  print 'This is Run method.'
