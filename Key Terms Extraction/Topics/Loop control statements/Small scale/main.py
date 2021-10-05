word = ''
minimum = None

while word != '.':

    word = input()
    if word == '.':
        break
    if minimum is None:
        minimum = float(word)
    elif minimum > float(word):
        minimum = float(word)

print(minimum)
