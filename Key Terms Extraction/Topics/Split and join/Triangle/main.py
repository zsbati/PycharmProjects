n = int(input())
line = ' ' * (2 * n - 1)
line = list(line)

for i in range(n):
    line[n + i - 1] = '#'
    line[n - i - 1] = '#'
    print(''.join(line))
