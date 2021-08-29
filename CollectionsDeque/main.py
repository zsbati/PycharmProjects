from collections import deque

n = int(input())
d = deque()

for i in range(n):
    li = input().split(" ")
    if li[0] == 'pop':
        d.pop()
    if li[0] == 'popleft':
        d.popleft()
    if li[0] == 'append':
        d.append(li[1])
    if li[0] == 'appendleft':
        d.appendleft(li[1])

print(' '.join(d))