def iterable(obj):
  try:
    iter(obj)
    return True
  except TypeError:
    return False

for element in [35,(34,),[4,5],(4,5),{"a":4},"abcd",4.5]:
  print(element, "is iterable:", iterable(element))
