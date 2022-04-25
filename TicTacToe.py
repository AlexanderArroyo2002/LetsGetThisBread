import random

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rows = [['-1-', '-2-', '-3-'],
        ['-4-', '-5-', '-6-'],
        ['-7-', '-8-', '-9-']]


def player_choice(choice):
    if 1 <= choice <= 3:
        rows[0][choice - 1] = ' X '
    elif 4 <= choice <= 6:
        rows[1][choice - 4] = ' X '
    elif 7 <= choice <= 9:
        rows[2][choice - 7] = ' X '
    else:
        print('Invalid answer. Pick a valid answer\n')


def bot_choice():
    try:
        choice = random.choice(choices)
        choices.remove(choice)
        if 1 <= choice <= 3:
            rows[0][choice - 1] = ' O '
        elif 4 <= choice <= 6:
            rows[1][choice - 4] = ' O '
        else:
            rows[2][choice - 7] = ' O '
        return choice
    except IndexError:
        print('I am out of choices!')
        exit()


def tic_tac_toe():
    used_numbers = set()
    bot_numbers = set()
    while True:
        print('You have chosen these numbers already:', ' '.join(used_numbers))
        print('The bot has chosen these numbers already:', ' '.join(bot_numbers))
        print('This is the current state of the board:')
        for i in range(len(rows)):
            print(' '.join(rows[i]))
        try:
            choice = int(input('Pick a number 1-9: '))
            print("")
            if str(choice) not in used_numbers and 1 <= choice <= 9 and str(choice) not in bot_numbers:
                used_numbers.add(str(choice))
                choices.remove(choice)
                player_choice(choice)
                bot_number = bot_choice()
                bot_numbers.add(str(bot_number))
            elif str(choice) in used_numbers:
                print('You already chose that number. Choose again')
            else:
                print('Invalid response. Try again.')
        except ValueError:
            print('Please enter a valid integer 1-9')


tic_tac_toe()
