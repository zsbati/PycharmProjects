import math
import os
import random
import re
import sys

def jumpingOnVClouds(c, k):
    e = 100  # initial energy level
    n = len(c)

    place = k % n
    if c[place] == 1:
        e -= 3
    else:
        e -= 1

    while place != 0:
        place = (place + k) % n
        if c[place] == 1:
            e -= 3
        else:
            e -= 1

    return e

k = 2
c = [0, 0, 1, 0, 0, 1, 1, 0]

print(jumpingOnVClouds(c, k))
