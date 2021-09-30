# the list "walks" is already defined
# your code here
sum_ = 0
for walk in walks:
    sum_ += int(walk.get("distance"))
print(sum_ // len(walks))
