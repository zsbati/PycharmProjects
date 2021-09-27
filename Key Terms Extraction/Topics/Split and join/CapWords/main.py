words = input().split("_")
out = ""
for word in words:
    out += word.lower().title()
print(out)
