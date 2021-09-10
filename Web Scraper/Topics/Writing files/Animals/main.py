# read animals.txt
# and write animals_new.txt

input_ = open('animals.txt', 'r', encoding='utf-8')
str_ = input_.read()
input_.close()

output_ = open('animals_new.txt', 'w', encoding='utf-8')
output_.write(str_.replace('\n', ' '))
output_.close()
