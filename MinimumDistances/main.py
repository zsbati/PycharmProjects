#!/bin/python3
import itertools
import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    mdist = -1

    comb = list(itertools.combinations(a, 2))

    equal = set()
    for i in range(len(comb)):
        li = list(comb[i])
        if li[0] == li[1]:
            equal.add(li[0])

    equals = list(equal)
    print(equals)
    if len(equals) == 0:
        return -1

    for i in range(len(equals)):

        index_list = list(filter(lambda x: a[x] == equals[i], range(len(a))))
        print(index_list)

        if mdist == -1:
            mdist = index_list[1] - index_list[0]


        if mdist > index_list[1] - index_list[0]:
            mdist = index_list[1] - index_list[0]

    return mdist

a = [7, 1, 3, 4, 1, 7]
print(minimumDistances(a))