# higher lower sart
import arts as art
from game_data import data
import random
import os


def random_selection():
    return random.choice(data)


def format_data(selection):
    name = selection['name']
    description = selection['description']
    country = selection['country']
    return f"{name}, a {description}, from {country}"


def check_guess(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    print(art.logo)
    score = 0

    selection_a = random_selection()
    selection_b = random_selection()
    game_on = True

    while game_on:
        selection_a = selection_b
        selection_b = random_selection()

        while selection_a == selection_b:
            selection_b = random_selection()

        print(f"Compare A: {format_data(selection_a)}.")
        print(f'{art.vs}'.center(40))
        print(f"Against B: {format_data(selection_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # get follower_count and call check guess to compare

        selection_a_count = selection_a['follower_count']
        selection_b_count = selection_b['follower_count']
        is_correct = check_guess(guess, selection_a_count, selection_b_count)

        os.system('clear')
        print(art.logo)
        if is_correct:
            score += 1
            print(f'Correct current score: {score}')
        else:
            game_on = False
            print(f'Sorry you got the wrong guess. Final score: {score}')
            print(art.over)


game()
