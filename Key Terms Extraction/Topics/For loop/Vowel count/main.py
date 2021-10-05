string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = set('aeiou')
letters = list(string)
count = 0
for letter in letters:
    if letter in vowels:
        count += 1
print(count)
