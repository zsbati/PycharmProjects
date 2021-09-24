# Write your code here
from lxml import etree
from nltk.tokenize import word_tokenize
from collections import Counter

xml_file = "news.xml"
root = etree.parse(xml_file).getroot()

articles = root[0]
titles = []
texts = []
for news in articles:
    titles.append(news[0].text)
    texts.append(news[1].text)

for i in range(len(titles)):
    printout = titles[i] + ':'
    body = texts[i].lower()
    words = word_tokenize(body)
    word_counter = Counter(words)
    print(word_counter.most_common(5))
