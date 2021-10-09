# write your code here
with open('salary.txt') as in_file, open('salary_year.txt', 'w') as out_file:
    monthly = in_file.read().split('\n')
    for salary in monthly:
        if salary != '':
            yearly = str(int(salary) * 12)
            out_file.write(yearly + '\n')
