def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["goat", "sheep", "dog", "cow", "dog", "dog"]
target = "dog"
target2 = 'cow'
result = linearSearchProduct(products, target)
print(result)