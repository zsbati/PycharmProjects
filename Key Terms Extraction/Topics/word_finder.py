from sklearn.feature_extraction.text import TfidfVectorizer

dataset = ["Yesterday",
           "All my troubles seemed so far away",
           "Now it looks as though they're here to stay",
           "Oh, I believe in yesterday"]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(dataset)
terms = vectorizer.get_feature_names()

# find (3, 11)

print(terms[11])
