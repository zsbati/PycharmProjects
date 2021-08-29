from collections import defaultdict
d = defaultdict(list)
arr1 = input().strip()
arr = arr1.split(" ")
n = int(arr[0])
m = int(arr[1])
A = []
for i in range(n):
    word = (input().strip())
    A.append(word)
    d[word].append(str(i+1))
B = []
for i in range(m):
    B.append(input().strip())

for i in range(m):
    li = (d.get(B[i]))
    s = ' '.join(li)
    print(s)
