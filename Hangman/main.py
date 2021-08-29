# Write your code here
import random

def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word_to_guess = 'javascript'  # random.choice(words)
    guess_set = set(word_to_guess)
    guesses = set()
    word_array = ['-' for i in word_to_guess]
    print('H A N G M A N')
    message = 'Input a letter: '

    trials = 8
    while trials > 0:
        print()
        print(''.join(word_array))
        letter = input(message, )

        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not letter.isalpha():
            print("Please enter a lowercase English letter")
            continue
        if letter.isalpha() and not letter.islower():
            print("Please enter a lowercase English letter")
            continue

        if letter in guess_set and letter not in guesses:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == letter:
                    word_array[i] = letter
        elif letter in guess_set and letter in guesses:
            print("You've already guessed this letter")
            if trials <= 0:
                print('You lost!')
                print()
                break
        else:
            if letter not in guesses:
                trials -= 1
                print("That letter doesn't appear in the word")
            else:
                print("You've already guessed this letter")
            if trials <= 0:
                print('You lost!')
                print()
                break
        guesses.add(letter)
        if guess_set.issubset(guesses):
            break

    if trials > 0:
        print('You guessed the word!')
        print('You survived!')



options = ["play", "exit"]
answer = ''
while answer != "exit":
    print('Type "play" to play the game, "exit" to quit:')
    answer = input()
    if answer == exit:
        break
    else:
        if answer == "play":
            game()
