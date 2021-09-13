from collections import Counter

frequencies = Counter(input().split())

print(frequencies.most_common(1)[0][0])
