import math
import os
import random
import re
import sys


# Complete the libraryFine function below. 1st returned, 2nd due
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2:
        return 0

    if y2 == y1 and m1 < m2:
        return 0

    if y1 <= y2 and m1 <= m2 and d1 <= d2:
        return 0

    if y1 == y2 and m1 == m2:
        if d1 > d2:
            return (d1-d2)*15
        else:
            return 0

    if y1 == y2:
        if m1 >= m2:
            return (m1-m2)*500
        else:
            return 0

    if y1 > y2:
        return 10000


d1 = 9
m1 = 6
y1 = 2015
d2 = 6
m2 = 6
y2 = 2015

print(libraryFine(d1, m1, y1, d2, m2, y2))