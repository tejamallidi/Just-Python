import sys
import random
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

# Write your code below this line 👇
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)

game_images = [rock, paper, scissors]

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
if user_choice < 0 or user_choice >= 3:
    sys.exit('You have entered a wrong number, please choose between 0, 1 and 2')

if user_choice == 0:
    print(f'\n {game_images[0]}')
elif user_choice == 1:
    print(f'\n {game_images[1]}')
else:
    print(f'\n {game_images[2]}')

if computer_choice == 0:
    print(f'Computer Chose \n {game_images[0]}')
elif computer_choice == 1:
    print(f'Computer Chose \n {game_images[1]}')
else:
    print(f'Computer Chose \n {game_images[2]}')


if computer_choice == user_choice:
    print('It\'s a draw')
elif computer_choice == 0 and user_choice == 2:  # Rock wins against scissors.
    print('You lose')
elif computer_choice == 1 and user_choice == 0:  # Paper wins against rock.
    print('You lose')
elif computer_choice == 2 and user_choice == 1:  # Scissors win against paper.
    print('You lose')
else:
    print('You Won')
