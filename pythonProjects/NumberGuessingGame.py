import random

print("Welcome to the Number Guessing Game!")
print("Please make all inputs as integers. Non-integer inputs will be truncated.")
min = int(input("Enter minimum range: "))
max = int(input("Enter maximum range: "))
number = random.randint(min, max)
guesses = 3
guess = number - 1
clues = 1

while guess != number and guesses > 0:
    if guesses == 2 and clues == 1:
        if guess < number:
            print("Clue #1: The number is greater than your current guess")
        else:
            print("Clue #1: The number is lesser than your current guess")
        clues = clues + 1
    elif guesses == 1 and clues == 2:
        print("Clue #2: The number ends in " + str(number % 10))

    print(str(guesses) + " guesses left")
    guess = int(input("Enter your guess: "))
    guesses = guesses - 1

    while guess > max or guess < min:
        guesses = guesses + 1
        guess = int(input("Guess out of range, please try again: "))

if guesses == 0 and guess != number:
    print("You failed, the number was " + str(number))
else:
    print("That's the right number!")
