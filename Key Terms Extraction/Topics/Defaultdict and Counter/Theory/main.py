#  You can experiment here, it won’t be checked
from collections import Counter
words = input().lower().split(' ')
freq_counter = Counter(words)
print(sorted(freq_counter.elements()))
