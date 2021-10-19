def check(num):
    if not num.isnumeric():
        print("It is not a number!")
    else:
        num = int(num)
        if num >= 202:
            print(num)
        else:
            print("There are less than 202 apples! You cheated me!")
