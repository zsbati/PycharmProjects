# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()

if operation in {'/', 'mod', 'div'} and second_number == 0:
    result = 'Division by 0!'
elif operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    result = first_number / second_number
elif operation == 'mod':
    result = first_number % second_number
elif operation == 'pow':
    result = first_number ** second_number
elif operation == 'div':
    result = first_number // second_number
else:
    result = 'invalid operation'
print(result)
