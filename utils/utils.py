"""Module for common helper and utility programs."""

import os
import config


def GetInputData(
    file_location, num_level_per_test, num_input_per_level=None, have_sep=True):
  """Generate input data from the input file.

  There can be multiple test cases and each test case can have multiple
  values as input, number of test cases and input per case can be large,
  so it parse the file incrementally and returns generators.

  Args:
    file_location: string, location of the input file relative to base dir,
        file is located on the same machine.
    num_level_per_test: int, number of input sections per test case.
    num_input_per_level: int, when number of input per level is fixed.
    have_sep: bool, in some cases there is no seperator between input data lines.

  Yields:
    List of list of input data.
  """
  file_path = os.path.join(config.GetProjectRootDir(), file_location)
  with open(file_path) as fp:
    num_test_cases = int(fp.readline().strip())
    for _ in xrange(num_test_cases):
      input = []
      for level in xrange(num_level_per_test):
        inp = []
        if have_sep:
          num_input_per_level = (
              num_input_per_level if num_input_per_level else int(fp.readline().strip()))
        for _ in xrange(num_input_per_level):
          inp.append(fp.readline().strip())
        input.append(inp)
      yield input
