import math

edge = int(input())

area = round(2 * math.sqrt(3.0) * math.pow(edge, 2), 2)

volume = round(math.sqrt(2.0) * math.pow(edge, 3) / 3, 2)

print(area, volume)
