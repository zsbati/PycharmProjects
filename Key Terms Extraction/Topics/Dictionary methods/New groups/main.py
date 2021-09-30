# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here

kindergarten = dict()
for group in groups:
    kindergarten[group] = None
n = int(input())
for i in range(n):
    kindergarten[groups[i]] = int(input())
print(kindergarten)
