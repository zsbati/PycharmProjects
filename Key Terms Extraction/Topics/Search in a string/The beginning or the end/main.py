string = input()
index_1 = string.find('old')
index_2 = string.rfind('old')
print(max(index_1, index_2))
