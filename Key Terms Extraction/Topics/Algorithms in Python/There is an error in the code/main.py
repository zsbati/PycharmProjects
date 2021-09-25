sentence = input()

def aver(sent):

    for sym in ['!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()

    total = 0
    for word in words:
        total = total + len(word)

    return total / len(words)

print(aver(sentence))
