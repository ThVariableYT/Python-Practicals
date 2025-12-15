# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'
print(string)
# matches all whitespace characters
pattern = '\s+'

# empty string
replace = '*'

new_string = re.sub(pattern, replace, string,3) 
print(new_string)
