# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
from collections import OrderedDict

firms = OrderedDict(json.loads(input()))

# your code here

# firms = OrderedDict({"YourHouse": 9.5, "BrownBuildCo": 9.1, "Build in the City": 9.0, "mr.Stone & Co": 7.8, "Flinstones Appartment": 7.3})
firms.popitem(last=True)
firms.popitem(last=True)
print(firms)
