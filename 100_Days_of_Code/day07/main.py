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
        print('GAME OVER, Hope you had fun')
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


def guess(let):
    letter = input("Guess a letter: ").lower()
    alphabet = string.ascii_lowercase
    if letter not in alphabet:
        print('You are only allowed to enter letters. Please Try Again')
    elif letter in let:
        print('You have already guessed that letter before.Try again!')
    print(
        f"You have guessed the letter \"{letter}\"")
    return letter


def game_play():

    welcome()

    letters_guessed = []
    chosen = chosen_word(words)
    my_choice = []
    my_choice = list('_' * len(chosen))

    # for i in range(len(chosen)):
    #     my_choice.append("_")
    count = 0
    lives = 7
    print(chosen)
    while lives:
        win = False
        correct = False
        print(f'You have {lives} lives')
        my_guess = guess(letters_guessed)
        for i in range(len(chosen)):
            if(chosen[i] == my_guess):
                my_choice[i] = my_guess
                print(my_choice)
                count += 1
                correct = True
        if not correct:
            lives -= 1
            letters_guessed.append(my_guess)
            print(arts[lives])

        if not lives:
            print("You Lost")
            print(f'The word is "{chosen}"')
            break

        if count == len(chosen):
            print(my_choice)
            print("You Win")
            break
    replay()


game_play()
