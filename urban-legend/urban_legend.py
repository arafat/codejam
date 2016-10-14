"""Implementation for Urban Legend problem from Google Code Jam.

Please refer Problem.txt for problem statement and
Solution.txt for solution algorithm.
"""

from utils import utils

_INPUT_TEST_DATA = 'urban-legend/testdata/input.txt'


def calculate_number_of_switch(search_engines, queries):
  """Calculates the number of switches.

  Considering the fact that implementation is optimized for number of switches.
  Also first choice of search engine will not be considered as a switch.
  Queries are processed in the order they appear.

  Args:
    search_engines: list of search engines.
    queries: list of queries to process.

  Returns: int, number of switches required.
  """
  engine = search_engines.copy
  switch = 0
  for q in queries:
    pass


if __name__ == '__main__':
  for search_engines, queries in utils.GetInputData(_INPUT_TEST_DATA, 2):
    number_of_switch = calculate_number_of_switch(search_engines, queries)
    print 'Number of switches required %s' %number_of_switch
  print 'Done'
