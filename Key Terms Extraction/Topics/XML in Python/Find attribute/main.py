from lxml import etree

root = etree.fromstring(input())
prop = input()

if root.get(prop) is not None:
    print(root.get(prop))
else:
    print('None')
