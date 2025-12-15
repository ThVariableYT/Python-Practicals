import re

pattern = '(h|a)h'
test_string = 'abdullah hah'
result = re.findall(pattern, test_string)
print(result)
'''if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	'''
