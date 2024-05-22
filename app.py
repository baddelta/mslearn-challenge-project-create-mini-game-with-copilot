import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ")
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ")
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 1
    else:
        return -1

def play_game():
    score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        if result == 1:
            print(f'You chose {user_choice}, computer chose {computer_choice}. You win!')
            score += 1
        elif result == -1:
            print(f'You chose {user_choice}, computer chose {computer_choice}. You lose!')
        else:
            print(f'You chose {user_choice}, computer chose {computer_choice}. It\'s a tie!')

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print(f'Your final score is: {score}')
            break

play_game()