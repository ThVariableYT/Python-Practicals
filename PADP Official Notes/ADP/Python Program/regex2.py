import re

string = 'hello 1 hi 89. Howdy 34'
pattern = '\d'

result = re.findall(pattern, string) 
print(result)
