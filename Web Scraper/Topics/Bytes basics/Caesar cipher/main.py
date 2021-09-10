feed = input()
out = ''
for char in feed:
    out += chr(ord(char) + 1)
print(out)
