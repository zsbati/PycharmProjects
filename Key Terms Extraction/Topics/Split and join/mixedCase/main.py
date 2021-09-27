words = input().split()
out = words[0]
for i in range(1, len(words)):
    out += words[i].title()
print(out)
