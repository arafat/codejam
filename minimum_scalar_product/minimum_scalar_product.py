def CalculateMinimumScalarProduct(scalar1, scalar2):
  scalar1 = sorted(scalar1)
  scalar2 = sorted(scalar2, reverse=True)
  return sum([i*j for i, j in zip(scalar1, scalar2)])
