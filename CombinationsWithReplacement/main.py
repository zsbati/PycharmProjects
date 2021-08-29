from itertools import combinations_with_replacement
stri = input().strip()
li = stri.split(" ")
k = int(li[1])
string = li[0]
li = list(string)
li.sort()
string = ''.join(li)

li = list(combinations_with_replacement(string, k))
li.sort()

for i in range(len(li)):
    print(''.join(li[i]))