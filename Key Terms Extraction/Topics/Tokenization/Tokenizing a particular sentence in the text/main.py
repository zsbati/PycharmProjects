from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize

text = "Meet the Greens! They've got a big house on the outskirts of Leeds. There are 15 rooms in it."

num = 2
words = sent_tokenize(text)
kutty = regexp_tokenize(text, r"[0-9A-z'\-]+")
#print(regexp_tokenize(sentence, r"[0-9A-z'\-]+"))
print(kutty)
