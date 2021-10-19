def check():
    x = input()
    try:
        num = int(x)
        if 25 <= num <= 37:
            print(num)
        else:
            raise ValueError
    except ValueError:
        print("Correct the error!")


