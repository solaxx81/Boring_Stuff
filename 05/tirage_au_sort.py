import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if random.randint(0,1):
        toss='heads'
    else:
        toss='tails'
    if toss == guess:
        print('You got it!')
        break
    else:
        print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
