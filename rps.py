import random


def game(player):
    if player != '1' and player != '2' and player != '3' and player != '4':
        print('Chose a valid number')
        return game(input('Please select 1(Rock) 2(Paper) 3(Scissors) 4(exit): '))
    else:
        if player == '4':
            exit()
        elif player == '1':
            playerChoise = 'Rock'
        elif player == '2':
            playerChoise = 'Paper'
        elif player == '3':
            playerChoise = 'Scissors'
        oneOf = ['Rock', 'Paper', 'Scissors']
        foe = random.choice(oneOf)
        print('You chose:', playerChoise)
        print('I chose:', foe)
        if (foe == 'Rock' and player == '1') or (foe == 'Paper' and player == '2') or (foe == 'Scissors' and player == '3'):
            print('tie')
        elif (foe == 'Rock' and player == '2') or (foe == 'Paper' and player == '3') or (foe == 'Scissors' and player == '1'):
            print('you win!')
        elif (foe == 'Rock' and player == '3') or (foe == 'Paper' and player == '1') or (foe == 'Scissors' and player == '2'):
            print('you lose... good luck next time')
        return game(input('Please select 1(Rock) 2(Paper) 3(Scissors) 4(exit): '))


game(input('Please select 1(Rock) 2(Paper) 3(Scissors) 4(exit): '))
