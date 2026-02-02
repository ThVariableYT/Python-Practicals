import re
string = "man and woman"
pattern = "man"
result=re.findall(pattern, string)
print(result)