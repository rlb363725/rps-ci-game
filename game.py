# Welcome and prompt
print(f"Hello, Welcome to the game!")

# Validate user input
valid_choices = ["rock", "paper", "scissors"]
invalid_choices = "Error, please choose rock, paper, scissors again" # Changed to a string

# Game loop
play_again = "yes"

while play_again == "yes":
    result = "It's a tie!"

    while result == "It's a tie!":
        user_choice = ""
        while user_choice not in valid_choices:
            user_choice = input(f"Please choose one of the following: {valid_choices}: ").strip().lower()
            if user_choice not in valid_choices:
                print(invalid_choices)

        print("---------")
        print(f"You chose: {user_choice}")

        # Generate computer choice
        computer_choice = random.choice(valid_choices)
        print("Computer chose:", computer_choice)
        print("---------")

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
            print("It's a tie! Let's play again! \n")

        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            print("You win! \n")

        else:
            result = "Computer wins!"
            print("Computer wins! \n")

    # Ask to play again
    while True:
        play_again = input("Thanks for playing! Would you like to play again? (yes/no): ").strip().lower()
        if play_again in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

print("---------")
print("Thanks for playing!")
print("---------")
print("Citations: Prof. Rossetti : Intro to Python and Applications: https://prof-rossetti.github.io/intro-software-dev-python-book/, Phyton.org Tutorial https://docs.python.org/3/tutorial/index.html, Google Gemini, Google Phyton Class https://developers.google.com/edu/python")
