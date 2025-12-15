import re

string = 'Twelve:12 Eighty nine:89.Nine:9'
pattern = '\d+'
#maxsplit=1
result = re.split(pattern, string,2) 
print(result)
