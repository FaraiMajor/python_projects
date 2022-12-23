# higher lower sart
from arts import vs, over, logo
from game_data import data
import random
import os


def random_selection():
    """Get data from random account"""
    return random.choice(data)


def format_data(selection):
    """Format account into printable format: name, description and country"""
    name = selection['name']
    description = selection['description']
    country = selection['country']
    return f"{name}, a {description}, from {country}"


def check_guess(guess, a_followers, b_followers):
    """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def replay():
    answer = input(
        'Do you want to play again? Enter Y for Yes or N for no: ').lower()
    if answer == 'y':
        game()
    else:
        print(over)


def game():
    print(logo)
    score = 0
    game_on = True
    selection_a = random_selection()
    selection_b = random_selection()

    while game_on:
        selection_a = selection_b
        selection_b = random_selection()

        while selection_a == selection_b:
            selection_b = random_selection()

        print(f"Compare A: {format_data(selection_a)}.")
        print(f'{vs}'.center(40))
        print(f"Against B: {format_data(selection_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # get follower_count and call check guess to compare

        a_follower_count = selection_a['follower_count']
        b_follower_count = selection_b['follower_count']
        is_correct = check_guess(guess, a_follower_count, b_follower_count)

        os.system('clear')
        print(logo)
        if is_correct:
            score += 1
            print(f'Correct current score: {score}')
        else:
            game_on = False
            print(f'Sorry you got the wrong guess. Final score: {score}')
    replay()


game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''


# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
# Get follower count.
# If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.
