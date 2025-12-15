print("----ITERABLES-------")
lst1=["Mumbai","Pune","Delhi","Patna"]
for city in lst1:
  print(city)

print("\n")

print("----ITERATORS-------")

iterator_obj=iter(lst1)
try:
  print(next(iterator_obj))
  print(next(iterator_obj))
  print(next(iterator_obj))
  print(next(iterator_obj))
  print(next(iterator_obj))
except:
  print("StopInteration Exception Raised")
