# Write your code here
from collections import OrderedDict

cards = int(input('Input the number of cards:\n'))
flashcards = OrderedDict()

for i in range(1, cards + 1):
    term = input('The term for card #'+str(i)+':\n')
    definition = input(f'The definition for card #{i}:\n')
    flashcards[term] = definition

for term in flashcards.keys():
    answer = input(f'Print the definition of \"{term}\":\n')
    if answer == flashcards[term]:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is \"{flashcards[term]}\".')
