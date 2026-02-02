# Program to remove all whitespaces
import re
# Multiline string
string = 'abc 12\ de 23 \n f45 6'
print(string)
# Matches with all whitespace characters
pattern = '\s+'

# Empty string
replace = '*'

new_string = re.sub(pattern, replace, string, 3)
print(new_string)