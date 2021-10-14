x = int(input())
y = int(input())

if x == 1 and y == 1:
    moves = 3
elif x == 1 and y == 8:
    moves = 3
elif x == 8 and y == 1:
    moves = 3
elif x == 8 and y == 8:
    moves = 3
elif x == 1 and y != 1 and y != 8:
    moves = 5
elif x == 8 and y != 1 and y != 8:
    moves = 5
elif y == 1 and x != 1 and x != 8:
    moves = 5
elif y == 8 and x != 1 and x != 8:
    moves = 5
else:
    moves = 8

print(moves)
