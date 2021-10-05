word = input()
inverted = word[::-1]
if word == inverted:
    print("Palindrome")
else:
    print("Not palindrome")
