import random

def computer_input():
    possible_choices = ['r','p','s']
    com = random.choice(possible_choices)
    return com

def decide(user, com):
    if user == com:
        if user == 'r':
            print("Both players choose rock. It's a tie!")
        elif user == 'p':
            print("Both players choose paper. It's a tie!")
        elif user == 's':
            print("Both players choose scissor. It's a tie!")
    elif user == 'r':
        print("Rock smashes scissor. You WIN!" if com == 's' else "Paper covers rock. You LOSE")
    elif user == 'p':
        print("Paper covers rock. You WIN!" if com == 'r' else "Scissor cuts paper. You LOSE")
    elif user == 's':
        print("Scissor cuts paper. You WIN!" if com == 'p' else "Rock smashes scissor. You LOSE")
    print('')

def play_game():
    print('ROCK PAPER SCISSOR GAME')
    print('Input --> r for rock / p for paper / s for scissor')
    
    user_choice = input('Please Input Your Choice : ').lower()
    if user_choice not in ['r','p','s']:
        print('Invalid Input')
        print("Restarting game...")
        print('')
        play_game()
    print('')

    com_choice = computer_input()
    decide(user_choice, com_choice)
    

# 3 rounds game
play_game()
play_game()
play_game()


