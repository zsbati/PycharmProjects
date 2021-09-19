import re

word = input()
# your code here
regex = r'the\b'
if re.match(regex, word) is not None:
    print('True')
else:
    print('False')
