# Take names of player
player1 = input('Enter player 1 name : ')
player2 = input('Enter player 2 name : ')


while True:
    # Take input from user about their choice
    guess1 = input(player1 + ' what is your choice - Rock, Paper or Scissor : ').upper()
    guess2 = input(player2 + ' what is your choice - Rock, Paper or Scissor : ').upper()

    if guess1 == guess2:
        print("It's a tie")
    elif guess1 == 'ROCK':
        if guess2 == 'SCISSOR':
            print(player1+' wins')
        elif guess2 == 'PAPER':
            print(player2+' wins')
    elif guess1 == 'SCISSOR':
        if guess2 == 'PAPER':
            print(player1+' wins')
        elif guess2 == 'ROCK':
            print(player2+' wins')
    elif guess1 == 'PAPER':
        if guess2 == 'ROCK':
            print(player1+' wins')
        elif guess2 == 'SCISSOR':
            print(player2+' wins')
    else:
        print('Invalid Input')
    playAgain = input('Do you want to play again ? Type Yes or No :').upper()
    if playAgain == 'YES':
        pass
    else:
        print('Game is finished')
        raise SystemExit



