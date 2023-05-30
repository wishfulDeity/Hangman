# Programming Assessment AS91896 Version 2
import random
import math


def check_guess():
    """Gets the current guess and checks if it's in the word.

    Also compares the 'guessed_letters' list to 'current_word'
    to see if the word has been guessed but not typed out yet.

    Returns:
        Bad (str): if lives is less than 1
        Good (str): if user_guess is equal to current_word
    """

    global lives

    if user_guess not in guessed_things:
        guessed_things.append(user_guess)

        # Check whether or not the guess is in the word.
        #
        # If yes, cool!
        # If the guess IS the word, end the game (good ending)
        # If no, too bad! Take a life away

        if user_guess == str(current_word):
            print(f'\nGood job! The word was {current_word}.\n')
            return 'Good'

        elif user_guess in current_word:
            if len(user_guess) == 1:
                print(f'\nNice! {user_guess} is in the word!\n')

            else:
                print(f'\n\'{user_guess}\' is in the word, but it\'s not '
                      'the whole word.')
                print('Please try again.')

        if user_guess not in current_word:
            if len(user_guess) == 1:
                print(f'\nUnlucky! \'{user_guess}\' isn\'t in the word.\n')
                lives -= 1
            else:
                print(f'Nope, \'{user_guess}\' isn\'t the word, try again.')

            if lives < 1:
                return 'Bad'

        if user_guess is None:  # <-- Unneeded? Maybe.
            pass
    else:
        print('\nYou have already guessed that, please try again.\n')

    print()


def ask_lives():
    """Get the amount of lives that the user wants.

    Returns:
        user_lives (int): if user_lives is greater than 0
        len(current_word) (int):  if user_lives is empty (equal to '')
    """

    global lives

    input('Press ENTER to play\n')
    print('\n' * 128)

    while lives == 0:
        try:
            user_lives = input('How many lives do you want?\n'
                               '(Enter nothing to generate it automatically '
                               'based on the length of the word) \n\n'
                               ' -- : ')

            if user_lives == 0 or user_lives == '':
                return math.ceil(len(current_word) * 1.5)

            elif int(user_lives) > 0:
                return int(user_lives)

        except ValueError:
            print('\nPlease enter a number.\n')
            continue


def hidden_print(string, list):
    """Print the word that the user has to guess in a way that they can't see
    (underscores where unguessed letters are)

    Also checks if the string is fully revealed,
    and changes the 'ending' variable accordingly

    Args:
        string (str): The word being printed
        list (list): The list of letters to print (make not underscored)"""

    global reveal_count  # <-- I hate this so much, make this local.
    global ending  # <-- This is fine tho

    # Loop through the string and print the character
    # if it that character shows up in the list
    for character in string:
        if character in list:
            print(character, end=' ')
        else:
            print("_", end=' ')

    if user_guess is not None:
        reveal_count += string.count(user_guess)

    # Debug prints vv
    print(f'\nLetters found: {reveal_count}')
    print(f'Word length: {len(string)}')

    print()


user_guess = None

words = []
guessed_things = []

with open('words.txt') as f:
    for line in f:
        words.append(line.strip())


current_word = random.choice(words).upper()
# current_word = 'fhqwhgads'.upper()  # Just for testing

reveal_count = 0  # Making this global hurts me

ending = None

print('\n' * 128)

# Intro text
print('\nPlease make your terminal window full screen (you\'ll need it)\n\n'
      'Welcome to Hangman!\n'
      'This game picks from around 1,200 of the most common English words.\n'
      'Not all of them are easy, so good luck!\n\n')

lives = 0
lives = ask_lives()
print('\n' * 128)

# Game loop
while ending is None:
    if lives >= 1:
        print(f'You have {lives} lives remaining.\n')

        hidden_print(current_word, guessed_things)

        if reveal_count == len(current_word):
            ending = 'Good'
            break

        # Print letters guessed so far
        print('\nLetters that you have guessed incorrectly so far: \n')
        for character in guessed_things:
            if len(character) == 1 \
                    and character not in current_word:
                print(character, end=' ')
        print()

        # Print words guessed so far
        print('\nWords that you have guessed so far: \n')
        for word in guessed_things:
            if len(word) > 1 \
                    and word is not current_word:
                print(word, end=' ')
        print()

        user_guess \
            = str(input('\nGuess a letter '
                        '(Or the whole word if you think you know it.)\n\n'
                        ' -- : ')).upper()

        print('\n' * 128)

        ending = check_guess()

        if ending is not None:
            break

print('\n' * 128)

if ending == 'Bad':
    print('You couldn\'t guess the word!')
    print(f'The word was \'{current_word}\'\n')

if ending == 'Good':
    print(f'Nice! You guessed it!! (congrats)\n')
