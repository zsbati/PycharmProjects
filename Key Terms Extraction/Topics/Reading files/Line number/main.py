# read sample.txt and print the number of lines
file = open('sample.txt', 'r')
counter = 0
for line in file:
    counter += 1

file.close()
print(counter)
