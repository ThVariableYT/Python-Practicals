import re

pattern = 'ma*n'
test_string = 'mn and woman'
result = re.findall(pattern, test_string)
print(result)
'''if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	'''
