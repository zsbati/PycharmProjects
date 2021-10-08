income = int(input())
tax = 0
percent = 0

if income <= 15527:
    percent = 0
    tax = 0
elif 15528 <= income <= 42707:
    percent = 15
    tax = income * percent / 100
elif 42708 <= income <= 132406:
    percent = 25
    tax = income * percent / 100
else:
    percent = 28
    tax = income * percent / 100

tax = round(tax)

output = f'The tax for {income} is {percent}%. That is {tax} dollars!'

print(output)
