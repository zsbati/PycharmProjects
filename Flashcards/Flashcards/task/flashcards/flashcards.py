# Write your code here
from collections import OrderedDict
import random

flashcards = OrderedDict()


def add():
    term_i = input('The card\n')
    while term_i in flashcards.keys():
        print('The card' + ' \"' + term_i + '\" ' + 'already exists. Try again:')
        term_i = input()
    definition_i = input('The definition of the card:\n')
    while definition_i in flashcards.values():
        print('The definition' + ' \"' + definition_i + '\" ' + 'already exists. Try again:')
        definition_i = input()
    flashcards[term_i] = definition_i
    print(f'The pair (\"{term_i}\":\"{definition_i}\") has been added.\n')


def remove():
    card = input('Which card?\n')
    if card not in flashcards.keys():
        print('Can\'t remove ' + card + ': there is no such card.')
    else:
        del (flashcards[card])
        print('The card has been removed.')


def ask():
    times = int(input('How many times to ask?\n'))
    for i in range(times):
        card = list(flashcards.keys())[random.randint(0, len(flashcards) - 1)]
        answer = input('Print the definition of "' + card + ' :\n')
        if answer == flashcards[card]:
            print('Correct!')
        else:
            if answer not in flashcards.values():
                print(f'Wrong. The right answer is \"' + flashcards[card] + '\".')
            else:
                for key, value in flashcards.items():
                    if value == answer:
                        correct_term = key
                        print(
                            f'Wrong. The right answer is \"{flashcards[card]}\", but your definition is correct for \"' + correct_term + '\".')


def export(file_name):
    with open(file_name, 'w') as opened_file:
        count = 0
        for card in flashcards.keys():
            opened_file.write(card + '\n')
            count += 1
            opened_file.write(flashcards[card] + '\n')
            count += 1
            cards = str(int(count / 2))
        print(f'{cards} cards have been saved.\n')


def read_in(file_name):
    with open(file_name, 'r') as opened_file:
        count = 0
        for line in opened_file:
            if count % 2 == 0:
                card = line.strip()
                count += 1
            else:
                definition = line.strip()
                flashcards[card] = definition
                count += 1
        cards = str(int(count / 2))
        print(f'{cards} cards have been loaded.\n')


while True:
    action = input('Input the action (add, remove, import, export, ask, exit):\n')
    if action == 'exit':
        print('Bye bye!')
        break
    if action == 'add':
        add()
    if action == 'remove':
        remove()
    if action == 'ask':
        ask()
    if action == 'export':
        file_name = input('File name:\n')
        export(file_name)
    if action == 'import':
        file_name = input('File name:\n')
        try:
            read_in(file_name)
        except FileExistsError:
            print('File not found.\n')
