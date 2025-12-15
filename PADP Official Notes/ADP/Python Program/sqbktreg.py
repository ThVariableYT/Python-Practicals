import re

pattern = '[cd]'
test_string = 'cssds'
result = re.findall(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
