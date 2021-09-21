file = open('animals.txt', 'r')
counter = 0
for line in file:
    if line.rstrip() == "summer":
        counter += 1
file.close()
print(counter)
