# work with the preset variable `words`
import re

# words = ['apple', 'pear', 'banana', 'Ananas']
words = [word for word in words if re.match(r'^[Aa]', word) is not None]
print(words)
