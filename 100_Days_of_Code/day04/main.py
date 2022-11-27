# ROCK PAPER SCISSORS

import random


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "rock vs paper->paper wins \n"
      + "rock vs scissor->rock wins \n"
      + "paper vs scissor -> scissor wins \n")
print("Game Options \n 0. rock \n 1. paper \n 2. scissors")
while True:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    game_images = [rock, paper, scissors]

    user_choice = int(input("Eneter a choice  (0 ,1, 2):\n"))
    computer_choice = random.randint(0, 2)
    computer_image = game_images[computer_choice]
    user_image = game_images[user_choice]

    print(f"You chose: \n{user_image}\n Computer chose: \n{computer_image}.")

    if user_choice >= 3 or user_choice < 0:
        print("Invalid number")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

    if not replay():
        print("\nThanks for playing")
        break
