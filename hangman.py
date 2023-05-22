# 21 Jack Segar-Farquharson
# Programming Assessment AS91896 Version 1
import random

# I was gonna use os.system('clear') to clear the terminal each turn
# But the 'clear' command is GNU/Linux only
# so I'll just use print('/n' * 128) or something in v2
#
# Using the wrong command doesn't even throw an exception
# so I can't use error capture on it.


def guess_letter_or_word():
    """Gets the user's input for a letter or word guess

    Returns:
        name (type): _description_
    """
    global user_guess

    user_guess = \
            str(input('\nGuess a letter '
                      '(Or the whole word if you think you know it.)\n\n'
                      '(If the word is completely revealed, '
                      'just enter the word.)\n\n'
                      'Automatic game completion coming soon!\n\n'
                      ' -- : '))

    if len(user_guess) == 1:
        if not user_guess.isalpha():
            print('\nGuess must be an alphabetical character.\n')
        else:
            return user_guess

    elif len(user_guess) > 1:
        contains_nonalphabetical = False

        for letter in user_guess:
            if not letter.isalpha():
                contains_nonalphabetical = True
                break

        if contains_nonalphabetical:
            print('\nGuess has impossible characters, please try again.\n'
                  '(must only contain letters)\n')


def check_guess():
    """Gets the current guess and checks if it's in the word.
    Also compares the 'guessed_letters' list to 'current_word'
    to see if the word has been guessed but not typed out yet.

    Returns:
        None if user_guess in (but not equal to) current_word.

        'Bad' if lives is less than 1.

        'Good' if user_guess is equal to current_word.
    """

    global lives

    if user_guess not in guessed_letters:
        guessed_letters.append(user_guess)

        # Check whether or not the guess is in the word.
        #
        # If yes, cool!
        # If the guess IS the word, end the game (good ending)
        # If no, too bad! Take a life away

        # TODO: Allow for spelling errors and have a
        # 'Did you mean _____?' thing
        if user_guess == str(current_word):
            print(f'\nGood job! The word was {current_word}.\n')
            return 'Good'

        elif user_guess in current_word:
            if len(user_guess) == 1:
                print(f'\nNice! {user_guess} is in the word!\n')
                return None

            else:
                print(f'\n\'{user_guess}\' is in the word, but it\'s not '
                      'the whole word.')
                print('Please try again.')
                return None

        if user_guess not in current_word:
            if len(user_guess) == 1:
                print(f'\nUnlucky! \'{user_guess}\' isn\'t in the word.\n')
                lives -= 1
            else:
                print(f'Nope, \'{user_guess}\' isn\'t the word, try again.')
                return None

            if lives < 1:
                return 'Bad'
            else:
                return None
    else:
        print('\nYou have already guessed that, please try again.\n')
        return None

    print()


def ask_lives():
    """Get the amount of lives that the user wants.

    Returns:
        user_lives if user_lives is greater than 0.

        len(current_word) if user_lives is empty (equal to '').
    """

    global lives

    start = input('Press ENTER to play\n')

    while lives == 0:
        try:
            user_lives = input('How many lives do you want?\n'
                            '(Enter nothing to generate it automatically '
                            'based on the length of the word) \n\n'
                            ' -- : ')

            if user_lives == 0 or user_lives == '':
                return len(current_word)

            elif int(user_lives) > 0:
                return int(user_lives)

        except ValueError:
            print('\nPlease enter a number.\n')
            continue


words = []
guessed_letters = []

with open('words.txt') as f:
    for line in f:
        if len(line) > 1:
            words.append(line.strip())

# TODO: Let the user pick a length of word to guess.
current_word = random.choice(words)

# current_word = 'test'  # Just for testing
ending = None

# Intro text
print('\nWelcome to Hangman!\n'
      'This game picks from the 30,000 most common English words.\n'
      'Not all of them are easy, so good luck!\n\n')

lives = 0
lives = ask_lives()

# Game loop
while ending is None:
    if lives >= 1:
        print(f'You have {lives} lives remaining.\n')

        # Print the word that the user has to guess in a way that
        # they can't see (underscores where unguessed letters are)
        for letter in current_word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print("_", end=' ')
        print()

        # Print the letters that the user has guessed so far.
        #
        # Only prints single characters, because "poleikts"
        # isn't really a 'letter', it's more a string
        #
        # Maybe have a guessed words area as well in future iterations?

        print('\nLetters that you have guessed incorrectly so far: \n')
        for character in guessed_letters:
            if len(character) == 1 \
                    and character not in current_word:
                print(character, end=' ')
        print()

        guess_letter_or_word()

        ending = check_guess()

    if ending == 'Bad':
        print('You couldn\'t guess the word!')
        print(f'The word was \'{current_word}\'\n\n')

    if ending == 'Good':
        print(f'Nice! You guessed it!! (congrats)\n\n')
