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
