def display(num):
    if num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'

    return num


for i in range(1, 101):
    print(display(i))
