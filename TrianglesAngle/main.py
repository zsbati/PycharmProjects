import math

x = int(input().strip())
y = int(input().strip())

kos = y/math.sqrt(x*x+y*y)

angle = round(math.acos(kos)*180.00/math.pi)

print(str(angle)+"\N{DEGREE SIGN}")