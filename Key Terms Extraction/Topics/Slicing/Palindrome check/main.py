# please work with the preset variable `word`
forward = word  # define here
lst = list(word)
lst.reverse()
backward = ''.join(lst)  # define here

if forward == backward:
    print("Yes")
else:
    print("No")
