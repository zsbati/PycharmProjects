# Write your code here
import string

from lxml import etree
import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
from nltk.corpus import stopwords

exclude = stopwords.words('english')

#print(exclude)

points = list(string.punctuation)
#print(points)
lemmatizer = WordNetLemmatizer()

xml_file = open("news.xml", 'r')
root = etree.parse(xml_file).getroot()

articles = root[0]
titles = []
texts = []
for news in articles:
    titles.append(news[0].text)
    texts.append(news[1].text)

for i in range(len(titles)):
    print(titles[i] + ':')
    body = texts[i].lower()
    tokenized = word_tokenize(body)
    lemmatized = [lemmatizer.lemmatize(word) for word in tokenized]
    words = [word for word in lemmatized if word not in exclude]
    words = [word for word in words if word not in points]
    words = sorted(words, reverse=True)
    word_counter = Counter(words)
    lst = word_counter.most_common(5)
    keywords = ''
    for item in lst:
        keywords += ' ' + item[0]
    print(keywords.strip())
    print()
