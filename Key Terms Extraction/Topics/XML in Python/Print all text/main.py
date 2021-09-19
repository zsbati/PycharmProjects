from lxml import etree


root = etree.fromstring(input())
Hprint(len(root), len(root.keys()))
