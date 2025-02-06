import random
# Greet the user and ask their name
print("Hello and welcome to the Number Guessing Game!")
name = input("What's your name?\n").strip().title()

# Explain game
print(f"Hello, {name}")
print("This game will choose a random number from 1-100. You'll be given 6 guesses. Don't worry I'll give you hints ")

# Choose a random number
rand_num = random.randint(1,100)

# Make a loop for the amount of guesses
for turns in range(6):
    # Print amount of guesses left
    print(f"\nYou have {6-turns} guesses left")  
    while True:
        try:
            # Ask user for a number
            user_num = int(input("Guess a number between 1 and 100:\n").strip())
            if user_num == rand_num:
                print("You got the number correct")
                break
            elif user_num > rand_num:
                print("Too high")
            elif user_num < rand_num:
                print("Too low")
            else:
                print(f"Ha, you lost. The number was {rand_num}")
        except ValueError:
            print("Invalid input.")

# Ask to play again