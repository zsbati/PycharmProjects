from lxml import etree

root = etree.fromstring(input())

children = root
for child in children:
    print(child.text)
