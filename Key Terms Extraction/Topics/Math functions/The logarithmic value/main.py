import math

arg = int(input())
base = int(input())

if base != 1 and base > 0:
    result = math.log(arg, base)
else:
    result = math.log(arg)

print(round(result, 2))
