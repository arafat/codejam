"""Implementation for Urban Legend problem from Google Code Jam.

Please refer Problem.txt for problem statement and
Solution.txt for solution algorithm.
"""

from utils import utils

_INPUT_TEST_DATA = 'urban-legend/testdata/input.txt'


def urban_legend():
  for search_engines, queries in utils.GetInputData(_INPUT_TEST_DATA, 2):

    pass


if __name__ == '__main__':
  urban_legend()
  print 'Done'
