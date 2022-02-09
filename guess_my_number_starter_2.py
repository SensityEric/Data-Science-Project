# Guessing Game

import random

secret_number = random.randrange(1,99)

guess_number = int(input('Enter the Secret Number between 1- 99: '))

while guess_number != secret_number:
    if guess_number > secret_number:
        print('the Number is too high')
        guess_number = int(input('Enter the Secret Number: '))
    else:
        print('The number is too low')
        guess_number = int(input('Enter the Secret Number: '))
print(f"Congratulation!!! You guess the Secret Number that is : {secret_number}  ")





