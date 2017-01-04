from timeit import timeit
from utils import utils

_INPUT_DATA_FILE_LOCATION = 'minimum_scalar_product/test_data/minimum_scalar_product.in'

def CalculateMinimumScalarProduct(scalar1, scalar2):
  scalar1 = sorted(scalar1)
  scalar2 = sorted(scalar2, reverse=True)
  print sum([i*j for i, j in zip(scalar1, scalar2)])

def Run():
  in_iter = utils.GetInputData(_INPUT_DATA_FILE_LOCATION, 1, 2)
  for input in in_iter:
    scalar1 = [int(i) for i in input[0][0].split(' ')]
    scalar2 = [int(i) for i in input[0][1].split(' ')]
    CalculateMinimumScalarProduct(scalar1, scalar2)
