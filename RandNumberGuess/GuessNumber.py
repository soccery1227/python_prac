import random

# Number guessing game within the range given by user
low = int(input("Enter the starting range of the numbers: "))
high = int(input("Enter the ending range of the numbers: "))

num = random.randint(low, high)
chances = 5
turns = 0

while turns < chances:
    turns += 1
    guess = int(input(f"Guess a number from {low} to {high}: "))

    if num == guess:
        print("You have guessed the right number!!")
        break
    elif turns >= chances and guess != num:
        print("Game over!!")
    elif guess > num:
        print("Guessed number too high!!")
    elif guess < num:
        print("Guessed number too low!!")
    else:
        print(f"Enter valid number in range {low} to {high} ")
