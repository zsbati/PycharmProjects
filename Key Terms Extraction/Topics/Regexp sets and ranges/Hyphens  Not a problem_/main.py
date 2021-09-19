import re

# your code here
word = input()
a = re.search('-', word, flags=0)
if a is not None:
    print('True')
else:
    print('False')
