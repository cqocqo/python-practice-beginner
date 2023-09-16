import random

number = random.randint(0, 100)

while True:
    guess = int(input('Guess the number between 1 to 100. '))
    if guess == number:
        print('congratulations! you have guessed it')
        break
    elif guess > number:
        print('too high')
    elif guess < number:
        print('too low')




