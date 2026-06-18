import random

secret_number = random.randint(1, 100)
attempts = 0
guess = 0  # Start with 0 so the loop begins

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess >= 1 and guess <= 100:
        attempts = attempts+1
        if guess == secret_number:
            print(f"You won! You guessed the number in {attempts} attempts")
        elif guess > secret_number:
            print("Your guess is higher than actual number")
        elif guess < secret_number:
            print("Your guess is lower than actual number")

    else:
        print("Enter a valid number")