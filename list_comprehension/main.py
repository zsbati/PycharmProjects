'''vowels = 'aeiou'
# create your list here
print([letter for letter in 'invertebrate' if letter in vowels])

# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]


binary_list = [1 if n > 0 else 0 for n in old_list]
print(binary_list)'''

text = ''
while text != '/exit':
    text = input()
    if text == '/help':
        print('The program calculates the sum of numbers')
        continue
    if text == "/exit":
        print('bye')
        break
    if text == '':
        continue
    numbers = [int(i) for i in text.split()]
    if len(numbers) == 1:
        print(text)
    else:
        sum_ = 0
        for n in numbers:
            sum_ += n
        print(sum_)