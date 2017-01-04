from utils import utils

_INPUT_DATA_FILE_LOCATION = 'minimum_scalar_product/test_data/minimum_scalar_product.in'

def CalculateMinimumScalarProduct(scalar1, scalar2):
  input = utils.GetInputData(_INPUT_DATA_FILE_LOCATION, 1, 2)
  import pdb; pdb.set_trace()
  scalar1 = sorted(scalar1)
  scalar2 = sorted(scalar2, reverse=True)
  return sum([i*j for i, j in zip(scalar1, scalar2)])
