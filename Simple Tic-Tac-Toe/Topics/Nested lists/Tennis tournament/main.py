n = int(input())
output = []
for i in range(n):
    game = input().split(' ')
    if game[1] == 'win':
        output.append(game[0])

print(output)
print(len(output))
