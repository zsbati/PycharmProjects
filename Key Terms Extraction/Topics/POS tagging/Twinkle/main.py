import nltk

# nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk.corpus import stopwords

exclude = stopwords.words('english')

poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']
poem = [word for word in poem if word not in exclude]
tags = nltk.pos_tag(poem)
for word in tags:
    if word[1] == 'NN':
        print(word[0])
