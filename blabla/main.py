'''colors = ("Purple", "Light blue", "Yellow")
color = None
while color not in colors:
    color = input()
if color == "Purple":
    print((160, 32, 255))
if color == "Light blue":
    print((80, 208, 255))
if color == "Yellow":
    print((255, 224, 32))'''

'''shopping_list = list(input().split())
shopping = dict()

for item in shopping_list:
    counter = 0
    for item1 in shopping_list:
        if item1 == item:
            counter += 1
    shopping.update({item: counter})

for item in shopping.keys():
    print(shopping.get(item), item)

limit = 25
numbers = []
while len(numbers) < 5:
    for i in range(limit):
        if i % 3 != 0:
            continue
        else:
            numbers.append(i)

print(len(numbers))'''

text = ""
while text != '/exit':
    text = input()
    if text == "/exit":
        print("bye")
        break
    if text == "":
        continue
    numbers = text.split()
    if len(numbers) == 1:
        print(text)
    else:
        [x, y] = numbers
        print(int(x) + int(y))



