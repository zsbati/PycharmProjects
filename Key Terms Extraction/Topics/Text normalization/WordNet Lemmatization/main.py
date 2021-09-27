from nltk.stem import WordNetLemmatizer
#import nltk
#nltk.download('wordnet')

# your code here
word = input()
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize(word, pos='n'))
print(lemmatizer.lemmatize(word, pos='a'))
print(lemmatizer.lemmatize(word, pos='v'))
