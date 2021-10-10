# write your code here

with open("users.json", "r") as json_file:
    users_dict_from_json = json.load(json_file)
    print(len(users_dict_from_json['users']))
