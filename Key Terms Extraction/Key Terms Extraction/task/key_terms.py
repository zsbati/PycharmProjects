# Write your code here
from lxml import etree
# import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
from collections import Counter

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
    words = sorted(word_tokenize(body), reverse=True)
    word_counter = Counter(words)
    lst = word_counter.most_common(5)
    keywords = ''
    for item in lst:
        keywords += ' ' + item[0]
    print(keywords.strip())
    print()
