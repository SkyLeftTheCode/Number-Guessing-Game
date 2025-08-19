import random  # Import random module to generate random numbers

# Introduction
print("HI! Welcome to number guessing game. Please ready.\n")

# Ask user for the lower and upper bound
low = int(input("Please enter Lower Bound : "))
print("")
high = int(input("Please enter Higher Bound : "))
print("")

# Game instructions
print(f"You have 7 chances to guess number between {low} and {high}. Let's start\n")

# Generate a random number within the given range
number = random.randint(low, high)

# Total number of chances
chance = 7
# Counter to track attempts used
counter = 0

# Game loop
while counter < chance:
    counter += 1  # Increment attempt counter

    # Take player's guess
    guess = int(input("Please enter your guess : "))
    print("")

    # Check if the guess is correct
    if guess == number:
        print(f"Correct! The number is {number}. You guessed it right in {counter} attempt(s).")
        break

    # If guess is wrong, give hints
    elif guess > number:
        print("Too high! Try a lower number.\n")
    elif guess < number:
        print("Too low! Try a higher number.\n")

# If all chances are used and number not guessed
if guess != number:
    print(f"Sorry! The number was {number}. Better luck next time.")
