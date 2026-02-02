import re

pattern = '^a...s$'
test_string = 'alias'
result = re.match(pattern, test_string)
print(result)
'''if result:
    print("Search successful.", result)
else:
    print("Search unsuccessful.")'''