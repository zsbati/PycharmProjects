import re

# your code here

name = input()

reg = '[B-N][aeiou]'

if re.match(reg, name):
    print('Suitable!')
