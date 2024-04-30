import random

def guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize the number of attempts and guessed number
    attempts = 0
    guessed_number = None
    
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while guessed_number != secret_number:
        try:
            # Ask the player to guess the number
            guessed_number = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guessed number is too high, too low, or correct
            if guessed_number < secret_number:
                print("Too low! Try again.")
            elif guessed_number > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

# Start the game
guessing_game()
