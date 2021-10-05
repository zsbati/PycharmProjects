symbols = list(input())
for symbol in symbols:
    if symbol in 'aeiou':
        print("vowel")
    elif symbol in 'bcdfghjklmnpqrstvxzwy':
        print("consonant")
    else:
        break
