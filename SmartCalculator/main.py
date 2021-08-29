text = ''
while text != '/exit':
    text = input()
    if text == '/help':
        print('The program calculates the sum of numbers')
        continue
    if text == "/exit":
        print('bye')
        break
    numbers = [int(i) for i in text.split()]
    if len(numbers) == 1:
        print(text)
    else:
        sum_ = 0
        for n in numbers:
            sum_ += n
        print(sum_)