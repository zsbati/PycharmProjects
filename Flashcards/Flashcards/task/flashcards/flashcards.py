# Write your code here
from collections import OrderedDict


class WrongTermError(BaseException):
    def __init__(self, expression):
        self.message = 'The term' + ' \"' + expression + '\" ' + 'already exists. Try again:'
        super().__init__(self.message)


class WrongDefinitionError(BaseException):
    def __init__(self, expression):
        self.message = 'The definition' + ' \"' + expression + '\" ' + 'already exists. Try again:'
        super().__init__(self.message)


flashcards = OrderedDict()

cards = int(input('Input the number of cards:\n'))
word_turns = 0
answer_turns = 0
while len(flashcards) < cards:
    if len(flashcards) == cards:
        break
    i = len(flashcards) + 1
    if word_turns == 0:
        word = input('The term for card #' + str(i) + ':\n')
    else:
        word = input()
    try:
        if word in flashcards.keys():
            word_turns += 1
            raise WrongTermError(word)
        else:
            term = word
            if answer_turns == 0:
                answer = input(f'The definition for card #{i}:\n')
            else:
                if len(flashcards) == cards:
                    break
                answer = input()
            try:
                if answer in flashcards.values():
                    answer_turns += 1
                    raise WrongDefinitionError(answer)
                else:
                    definition = answer
                    flashcards[term] = definition
                    word_turns = 0
                    answer_turns = 0
                    if len(flashcards) == cards:
                        break
            except WrongDefinitionError as err:
                if len(flashcards) == cards:
                    break
                print(err)

    except WrongTermError as err:
        if len(flashcards) == cards:
            break
        print(err)


for term in flashcards.keys():
    answer = input(f'Print the definition of \"{term}\":\n')
    if answer == flashcards[term]:
        print('Correct!')
    else:
        if answer not in flashcards.values():
            print(f'Wrong. The right answer is \"{flashcards[term]}\".')
        else:
            for key, value in flashcards.items():
                if value == answer:
                    term = key
            print(
                f'Wrong. The right answer is \"{flashcards[term]}\", but your definition is correct for \"' + term + '\".')
