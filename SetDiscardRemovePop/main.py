n = int(input())
s = set(map(int, input().split()))
ops = int(input())   # number of operations
for i in range(ops):
    op = input()
    o = op.split(" ")
    if o[0] == "pop":
        s.pop()
    if o[0] == "remove":
        s.remove(int(o[1]))
    if o[0] == "discard":
        s.discard(int(o[1]))

print(sum(s))
