# write your code here

def index(int_1, int_2):
    if int_1 == 0:
        return int_2
    elif int_1 == 1:
        return int_2 + 3
    elif int_1 == 2:
        return int_2 + 6
    else:
        return None


winners = []


def check_rows(array):
    if array[0] == array[1] == array[2] and array[0] != '_':
        winners.append(array[0])
    if array[3] == array[4] == array[5] and array[3] != '_':
        winners.append(array[3])
    if array[6] == array[7] == array[8] and array[6] != '_':
        winners.append(array[6])


def check_columns(array):
    if array[0] == array[3] == array[6] and array[0] != '_' and array[0] != ' ':
        winners.append(array[0])
    if array[1] == array[4] == array[7] and array[1] != '_' and array[1] != ' ':
        winners.append(array[3])
    if array[2] == array[5] == array[8] and array[2] != '_' and array[2] != ' ':
        winners.append(array[2])


def check_main_diagonal(array):
    if array[0] == array[4] == array[8] and array[0] != '_' and array[0] != ' ':
        winners.append(array[0])


def check_secondary_diagonal(array):
    if array[2] == array[4] == array[6] and array[2] != '_' and array[2] != ' ':
        winners.append(array[2])


def checks(array):
    check_rows(array)
    check_columns(array)
    check_main_diagonal(array)
    check_secondary_diagonal(array)


def draw(array):
    print('---------')
    for i in range(3):
        line = '|'
        for j in range(3):
            line += ' ' + cells[index(i, j)]
        line += ' ' + '|'
        print(line)
    print('---------')


cells = input('Enter cells: ', )

checks(cells)

draw(cells)

if abs(cells.count('X') - cells.count('O')) > 1:
    print('Impossible')
elif len(winners) == 0 and '_' not in cells and ' ' not in cells:
    print('Draw')
elif len(winners) == 0 and ('_' in cells or ' ' in cells):
    print('Game not finished')
elif len(winners) > 1:
    print('Impossible')
else:
    print(winners[0], 'wins')
