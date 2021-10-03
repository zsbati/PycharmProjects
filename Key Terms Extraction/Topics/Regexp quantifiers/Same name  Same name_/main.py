import re


# put your regex in the variable template
template = "[A-Z][a-z]{1,} |[A-Z][a-z]{1,} [A-Z][a-z]{1,} " + 'Smith'
#print(re.match(template, input()) is not None)
