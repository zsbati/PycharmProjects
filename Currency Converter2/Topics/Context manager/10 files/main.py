# write your code here
for i in range(1, 11):
    name = 'file' + str(i) + '.txt'
    file_i = 'file' + '_i'
    with open(name, 'w', encoding='utf-8') as file_i:
        file_i.write(str(i))
