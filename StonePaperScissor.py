#!usr/bin/python3
from random import randint

def Choose_winner(player_option, bot_option):
    if bot_option is player_option:
        print("It's a Tie")
    elif bot_option%3 is player_option or bot_option%3 is player_option:
        print("You Won")
    else:
        print("Bot Won!")

def start_game():
    print("**** Game Starts ****")
    print("Choose anyone")
    print('1. Stone')
    print('2. Paper')
    print('3. Scissor')
    player_option = int(input("Your Option: "))
    bot_option = randint(1,3)
    print("Bot Option: " + str(bot_option))
    Choose_winner(player_option, bot_option)

def main():
    print('**** Menu ****')
    print('1. Play')
    print('2. Rules')
    print('3. Exit')
    choice = int(input('Enter your Choice: '))
    if choice is 1:
        start_game()
    elif choice is 2:
        rules()
    elif choice is 3:
        exit()

if __name__ == '__main__':
    main()
