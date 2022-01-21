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


## Commentary
"""
Line 1:
    Line 1 imports the random library which allows our code to randomly select
    a number and assign it to a variable depending on a particular range. 
    
Line 3:
    A generic print statement that welcomes users to the game.

Line 4:
    Accept input (yes/no) from the user to tell whether they want to read the game
    manual or not. i thought this was efficient to describe the necessary inputs
    required from the user.

Line 6-13:
    This block of code is an if statement that evaluates the input from line 4. If
    the user input is 'yes', the print statement below it runs and displays the game
    manual, else the program just continues. 

Line 15:
    This code accepts input from the user to tell whether they are ready to begin
    play. 

Line 16-17:
    The input from line 15 is evaluated. The block of code allows the program to 
    continue to run if the user inputs 'yes', but quits on any other input.

Line 19:
    The upper range for the guess range is assigned to a variable after the input is
    collected from the user. 

Line 20-27:
    The block of code here first checks to see if the number is an integer using the
    isdigit() method (Line 21). If it is, it is then cast into the user_guess variable
    as an integer (Line 22). The variable is again checked to be sure the value is greater
    than zero since the lower range of the random library method used is 0 (Line 23).
    If it isn't, the user is asked to enter a number greater than zero (Line 23-24). If
    however the user enters anything that is not an integer, the code from line 21-25 
    fails to run and the user is asked to enter a number (Line 27).

Line 29:
    A global variable is declared to hold the number of guesses the user makes to get
    the correct number. 

Line 30-47:
    The block of code here begins as a while loop to allow us make use of the continue 
    keyword to restart the loop at some points (Line 30). Line 31 adds 1 to the number
    of guesses the user makes at every loop since each loop means the user wants to make
    another guess. Line 32 collects the user guess an input, and if it's a number, it's 
    converted from string to integer in line 33. Else, the user is prompted to enter a
    number (Line 36). The continue keyword runs through the while loop again, adding one 
    to the number of guesses and providing the user with another option to enter an
    input. If the input was a number, it is checked against the random number generated,
    and if correct, 'You got it!' is printed to the screen. The block of code from line
    42-47 checks to see whether number was greater or less than the guess and prints the
    required output, making the guess easier for the user.
    
Line 49-52:
    This block of code executes after the correct number is guessed. Using a simple if
    function, it evaluates the number of guesses; if the number of guesses is exactly one,
    it prints out the statement in line 50, else the statement in line 52 prints. 
"""