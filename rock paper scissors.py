# Rock, Paper, Scissors Game
from random import randint

moves = ['rock', 'paper', 'scissors']

while True:
    computer = moves[randint(0,2)]
    player = input('rock, paper or scissors? (or end the game) ').lower()
    if player == 'end the game':
        print('the game has ended')
        break
    elif player == computer:
        print('tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('HAHA LOSER!', computer, 'beats', player)
        else:
            print('you win!', player, 'beats', computer)
    elif player == 'paper':
        if computer == 'scissors':
            print('HAHA LOSER!', computer, 'beats', player)
        else:
            print('you win!', player, 'beats', computer)
    elif player == 'scissors':
        if computer == 'rock':
            print('HAHA LOSER', computer, 'beats', player)
        else:
            print('you win!', player, 'beats', computer)
    else:
        print('check your spelling...')