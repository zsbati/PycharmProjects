# read sums.txt
file = open('sums.txt', 'r')

for line in file:
    numbers = line.split(' ')
    int_0 = int(numbers[0])
    int_1 = int(numbers[1])
    print(int_0 + int_1)

file.close()
