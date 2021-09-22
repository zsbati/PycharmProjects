from nltk.tokenize import regexp_tokenize

sentence = input()
#sentence = "We were on the Queen Elizabeth, coming back from our first trip to Europe."
num = int(input())
#num = -1

kutty = regexp_tokenize(sentence, "[A-z]+")

print(kutty[num])
