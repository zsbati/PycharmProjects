from collections import Counter
words = input().lower().split(' ')
frequencies = Counter(words)
print(sorted(frequencies.elements()))
