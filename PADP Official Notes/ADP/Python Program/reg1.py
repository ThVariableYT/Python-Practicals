import re

pattern = '(a*)cb$'   #for starting character use caret symbol
test_string = 'aacb'
result = re.match(pattern, test_string)

if result:
  print("Search successful.",result)
else:
  print("Search unsuccessful.")	
