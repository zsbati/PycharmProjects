import math

x = float(input())

sigma = round(1.0 / (1.0 + math.exp(-x)), 2)

print(sigma)
