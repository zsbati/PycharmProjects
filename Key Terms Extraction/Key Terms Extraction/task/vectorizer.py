from sklearn.feature_extraction.text import TfidfVectorizer

dataset = open('words.txt', 'r')

vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True,
                             analyzer='word', ngram_range=(1, 1),
                             stop_words=None)
tfidf_matrix = vectorizer.fit_transform([dataset])

print(tfidf_matrix)
