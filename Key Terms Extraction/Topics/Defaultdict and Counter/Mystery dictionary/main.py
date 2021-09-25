# `random_dict` has been defined
# the input is in the variable `word`
# write the rest of the code here

random_dict.setdefault(word, '0')

if random_dict.get(word) != '0':
    print(random_dict.get(word))
else:
    print('Not in the dictionary')

