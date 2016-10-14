"""Module for common helper and utility programs."""

import os


_BASE_DIR_NAME = 'codejam'


def GetBaseDirPath(path):
  """Construct base directory path, on the basis of base dir name.

  Assumption is that there is only one directory with base dir name.

  Args:
    path: string, path to construct base dir path.

  Returns:
    String representing absolute path for base directory.
  """
  abspath = os.path.abspath(path)
  return abspath[:abspath.index(_BASE_DIR_NAME) + len(_BASE_DIR_NAME)]

  
def GetInputData(file_location, num_level_per_test):
  """Generate input data from the input file.

  There can be multiple test cases and each test case can have multiple
  values as input, number of test cases and input per case can be large,
  so it parse the file incrementally and returns generators.

  Args:
    file_location: string, location of the input file relative to base dir,
        file is located on the same machine.
    num_level_per_test: int, number of input sections per test case.

  Yields:
    List of list of input data. 
  """
  file_path = os.path.join(GetBaseDirPath(__file__), file_location)
  with open(file_path) as fp:
    num_test_cases = int(fp.readline().strip())
    for _ in xrange(num_test_cases):
      input = []
      for level in xrange(num_level_per_test):
        line = fp.readline()
        inp = []
        for _ in xrange(int(line.strip())):
          inp.append(fp.readline().strip())
        input.append(inp)
      yield input


if __name__ == '__main__':
  print 'I am in main.'
  gen = GetInputData('urban-legend/testdata/input.txt', 2)
  import pdb; pdb.set_trace()
  print 'Done'