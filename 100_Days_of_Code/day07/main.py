# hangman
import random
import hangman_words as words
import hangman as art
import string


arts = art.stages


def chosen_word(words):
    word = random.choice(words.word_list)
    return word


def replay():
    res = input(
        "Do you want to play again? Enter 'Y' for Yes or 'N' for No: ").lower()

    if res == 'y':
        game_play()
    else:
        print('GAME OVER, Hope yout had fun')
        print(art.logo)


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


def guess():
    letter = input("Guess a letter: ").lower()
    print(
        f"You have guessed the letter \"{letter}\"")
    return letter


def game_play():

    welcome()
    alphabet = string.ascii_lowercase
    my_choice = []
    letters_guessed = []
    chosen = chosen_word(words)

    for i in range(len(chosen)):
        my_choice.append("_")

    lives = len(arts)
    while lives > 0:
        print('You have ' + str(lives) + ' tries')
        for i in range(len(chosen)):
            if(chosen[i] == guess()):
                print(f"letter \"{chosen[i]}\" is in the word")
                my_choice[i] = guess()
            else:
                lives -= 1
                print(arts[lives])

        if lives < 0:
            break
        print(my_choice)

        replay()


game_play()
