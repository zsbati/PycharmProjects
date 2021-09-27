dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
words = input().split()
count = 0
for word in words:
    if word not in dictionary:
        print(word)
        count += 1
if count == 0:
    print("OK")
