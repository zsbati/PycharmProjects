key = int(input())

if key in squares.keys():
    print(squares.get(key))
    squares.pop(key)
else:
    print('There is no such key')

print(squares)
