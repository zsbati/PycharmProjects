from nltk.tokenize import regexp_tokenize


print(regexp_tokenize(input(), r"[0-9A-z'\-]+"))
