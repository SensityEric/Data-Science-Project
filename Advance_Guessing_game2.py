#Advanced Guessing Game

secret_number = 9

game_count = 0
game_limit = 3

while game_count < game_limit:
    guess = int(input("Guess: "))
    game_count += 1
    print(f"  {game_count} chance gone")
    if guess == secret_number:
        print('You won')
        break
else:
    print('Sorry try Again')
