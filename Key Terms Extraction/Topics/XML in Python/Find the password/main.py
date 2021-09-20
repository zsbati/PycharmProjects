from lxml import etree


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    for e in root:
        if e.get('password'):
            return e.get('password')
    return None
