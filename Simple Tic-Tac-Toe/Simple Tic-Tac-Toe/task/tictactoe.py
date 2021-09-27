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
    if array[0] == array[1] == array[2] and (array[0] == 'X' or array[0] == 'O'):
        winners.append(array[0])
    if array[3] == array[4] == array[5] and (array[3] == 'X' or array[3] == 'O'):
        winners.append(array[3])
    if array[6] == array[7] == array[8] and (array[6] == 'X' or array[6] == 'O'):
        winners.append(array[6])


def check_columns(array):
    if array[0] == array[3] == array[6] and (array[0] == 'X' or array[0] == 'O'):
        winners.append(array[0])
    if array[1] == array[4] == array[7] and (array[1] == 'X' or array[1] == 'O'):
        winners.append(array[1])
    if array[2] == array[5] == array[8] and (array[2] == 'X' or array[2] == 'O'):
        winners.append(array[2])


def check_main_diagonal(array):
    if array[0] == array[4] == array[8] and (array[0] == 'X' or array[0] == 'O'):
        winners.append(array[0])


def check_secondary_diagonal(array):
    if array[2] == array[4] == array[6] and (array[2] == 'X' or array[2] == 'O'):
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
            line += ' ' + array[index(i, j)]
        line += ' ' + '|'
        print(line)
    print('---------')


cells = '_________'

draw(cells)

count = 0

while True:

    if len(winners) != 0:
        print(winners[0] + ' wins')
        break
    if cells.count('X') + cells.count('O') >= 9:
        if len(winners) == 0:
            print('Draw')
        break
    places = list(cells)
    site = input('Enter the coordinates:', ).split()
    if len(site) != 2:
        print('You should enter numbers!')
        continue
    if not site[0].isnumeric() or not site[1].isnumeric():
        print('You should enter numbers!')
        continue
    if site[0] not in ['1', '2', '3'] or site[1] not in ['1', '2', '3']:
        print('Coordinates should be from 1 to 3!')
        continue
    if site[0] in ['1', '2', '3'] and site[1] in ['1', '2', '3']:
        ind = index(int(site[0]) - 1, int(site[1]) - 1)
        if cells[ind] == ' ' or cells[ind] == '_':

            if count % 2 == 0:
                places[ind] = 'X'
            else:
                places[ind] = 'O'
            count += 1
            cells = ''.join(places)
            draw(cells)
            checks(cells)

        else:
            print('This cell is occupied! Choose another one!')
            continue
