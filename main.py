import random

print("\nWelcome to the Number Guessing Game!")
read_manual = input("Read instructions? (yes/no): ")

if read_manual.lower() == "yes":
     print("\n The Game Manual:"
           "\n ==========================================="
           "\n You'll be asked to set a guess range."
           "\n The number you choose is your upper limit."
           "\n Guess a number from 0 to the input. Your"
           "\n final score is calculated per your number"
           "\n of inputs")

ready_player = input("\nOkay, Ready? (yes/no): ")
if ready_player.lower() != "yes":
    quit()

user_range = input("\nSet a guess range: ")
if user_range.isdigit():
    user_range = int(user_range)
    if user_range > 0:
        random_number = random.randint(0, user_range)
    else:
        print("Enter a number greater than 0.")
else:
    print("Enter a number!")

num_of_guesses = 0;
while True:
    num_of_guesses += 1
    user_guess = input("Enter a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number!")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You guessed above the right number.")
        continue
    else:
        print("You guessed below the right number.")
        continue

if num_of_guesses == 1:
    print("\nYou guessed the correct number in one attempt. You're awesome!")
else:
    print("You guessed the correct number in", num_of_guesses, "guesses.")