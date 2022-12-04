# hangman
import random
import hangman_words as words
import hangman as art
import string

# saves all the stages of the hangman
arts = art.stages

# get a random word from a list of words in the hangman_words.py module


def chosen_word(words):
    word = random.choice(words.word_list)
    return word

# prompts user to play again


def replay():
    res = input(
        "Do you want to play again? Enter 'Y' for Yes or 'N' for No: ").lower()

    if res == 'y':
        print(art.logo)
        game_play()
    else:
        print('GAME OVER, Hope you had fun')
        print(art.over)

# welcome screen to give a user name and print game rules


def welcome():

    # Define a name variable
    name = input("""
                ================================================================
                > Welcome to the Hangman Game! Please Enter your preferred game name:  <
                """).capitalize()

    # Use a decision making process to accept only alphabets as name
    if name.isalpha() == True:
        print(art.logo)
        print(""">> Hi!""", name, """Glad to have you here! <<<
                You will be playing against the computer today.
                The computer will randomly choose a word and you will try to guess what the word is.
                You can always invite your friends for a fun time together
                ==========================================================
                Good Luck! Have fun playing""")

    else:
        print('Please enter your name using letter only')
        name = input('Enter a game name here:  ')
        print('Hi!', name, 'Please go through the rules of the game')

# guess letter


def guess(let):
    letter = input("Guess a letter: ").lower()
    # Define a variable alpahabet
    alphabet = string.ascii_lowercase
    if letter not in alphabet:
        print('You are only allowed to enter letters. Please Try Again')
    elif letter in let:
        print('You have already guessed that letter before.Try again!')
    print(
        f"You have guessed the letter \"{letter}\"")
    return letter


welcome()


def game_play():
    # call the welcome function to get the game running

    # letter_guessed list saves all the letters the user has guessed and when user repeats the same letter a message will remind them
    letters_guessed = []
    chosen = chosen_word(words)

    # my_choice list stores all the correct guess that we encounter
    my_choice = []
    my_choice = list('_' * len(chosen))

    # for i in range(len(chosen)):
    #     my_choice.append("_")

    # count keeps tracks of all the right words guessed
    count = 0
    lives = len(arts)

    print('The word contains', len(chosen), 'letters.')
    while lives:
        # this boolean track whether our guess is true or not in the loop.
        correct = False
        print(f'You have {lives} lives')
        my_guess = guess(letters_guessed)

        # loop to check the guessed letter against all the letters in the random word
        for i in range(len(chosen)):
            if(chosen[i] == my_guess):
                my_choice[i] = my_guess
                letters_guessed.append(my_guess)
                print(my_choice)
                count += 1
                correct = True
    # when a guess is incorrect subtract 1 life and print the hangman part
        if not correct:
            lives -= 1
            letters_guessed.append(my_guess)
            print(my_choice)
            print(arts[lives])
# when all lives are used then game is over
        if not lives:
            print(art.lost)
            print(f'The word is "{chosen}"')
            break

        # if the word matched the random word then you win
        final_word = ''.join(my_choice)
        if count == len(chosen):
            if final_word == chosen:
                print(art.won)
                print(final_word)
                break

# prompts user to play again
    replay()


# Full program run
game_play()
