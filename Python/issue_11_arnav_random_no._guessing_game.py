import random

def number_guessing_game():
    """
    A fun, command-line number guessing game with unlimited attempts and Quiting Option.
    """

    print("\n 🌟 Welcome to the Ultimate Number Guessing Challenge! 🌟\n")

    # --- Game Setup ---
    LOWER_BOUND = 1
    UPPER_BOUND = int(input("Enter the last number of the range: "))
    
    # Generate the secret random number
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    
    # Initialize game variables
    attempts = 0
    guess = None
    
    # --- Introduction and Instructions ---
    print('\n')
    print("-" * 50,)
    print(f"I've secretly picked a number between **{LOWER_BOUND}** and **{UPPER_BOUND}**.")
    print("Guess as many times as you need! The attempt counter is hidden. 🤔")
    print("-" * 50)
    
    # --- Main Game Loop ---
    while guess != secret_number:

        guess_input = input("\nEnter your guess or q to Quit : ")

        # Command--To--Quit
        if guess_input.lower() in ['q','quit']:
                print(f"\n💔 Game Over. You quit after {attempts} attempts.")
                print(f"The secret number was **{secret_number}**.")
                break #Exits the Loop
        try:
            # Convert the input to an integer
            guess = int(guess_input)
            
            # Increment the attempt counter (it's a secret!)
            attempts += 1
            
            # --- Provide Hints ---    
            if guess < LOWER_BOUND or guess > UPPER_BOUND:
                print(f"🚨 Hold on! Your guess must be between {LOWER_BOUND} and {UPPER_BOUND}. Try again.")
                # Don't count invalid range input as a real attempt
                attempts -= 1 
            elif guess < secret_number:
                print("⬇️ Too low! Go higher, you can do it! ⬆️")
            elif guess > secret_number:
                print("⬆️ Too high! Time to come down a bit. ⬇️")
            
                
        except ValueError:
            # Handle non-integer input (e.g., text)
            print("🛑 Invalid input! Please enter a whole number.")

    # --- Game Over (Success) ---
    print("\n🎉 CONGRATULATIONS! YOU GOT IT! 🎉")
    print(f"The secret number was indeed **{secret_number}**.")
    print(f"You guessed it in just **{attempts}** attempts!")
    
    # --- Quick Feedback ---
    if attempts <= 5:
        print("That was incredibly fast! You must be a guessing genius! 🧠")
    elif attempts <= 10:
        print("A solid performance! Well done!")
    else:
        print("You got there in the end! Persistence pays off! 👍")
    
    # --- Option to Play Again ---
    print("-" * 50)
    play_again = input("Wanna play another round? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        print("\nStarting a new game...")
        number_guessing_game() # Recursive call If want to restart
    else:
        print("Thanks for playing! See you next time! 👋")

# --- Start the Game ---
if __name__ == "__main__":
    number_guessing_game()