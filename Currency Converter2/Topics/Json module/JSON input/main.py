import json


# write your code here

json_str = input()
obj = json.loads(json_str)
print(type(obj))
print(obj)
