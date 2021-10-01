import nltk

sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']
words = nltk.pos_tag(sent)
for word in words:
    if word[0] == 'raced':
        print(word[1])
        break
