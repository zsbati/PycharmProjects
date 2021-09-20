#  You can experiment here, it won’t be checked
from lxml import etree

xml_string = '<team name="Breakfast Club"><members><member name="Judd"/><member name="Ally"/><member name="Anthony"/><member name="Molly"/><member name="Emilio"/></members></team>'

root = etree.fromstring(xml_string)

names = ''

members = root[0]

for member in members:
    names += ' ' + member.get('name')

print(names.strip())
