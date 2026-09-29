import random

# Game choices
choices = {
    "snake": 1,
    "water": -1,
    "gun": 0
}

# Reverse dictionary for displaying choices
reverse_choices = {
    1: "snake",
    -1: "water",
    0: "gun"
}

# Computer randomly chooses
computer = random.choice([1, -1, 0])

# Take user's choice
youstr = input("Enter your choice (snake, water, gun): ").lower().strip()

# Check if user's choice is valid
if youstr not in choices:
    print("Invalid choice! Please enter snake, water, or gun.")

else:
    # Convert user's choice into number
    you = choices[youstr]

    # Display choices
    print(f"\nComputer chose: {reverse_choices[computer]}")
    print(f"You chose: {reverse_choices[you]}")

    # Tie
    if computer == you:
        print("It's a tie! 🤝")

    # User wins
    elif (
        (computer == -1 and you == 1) or   # Snake beats Water
        (computer == 1 and you == 0) or    # Gun beats Snake
        (computer == 0 and you == -1)      # Water beats Gun
    ):
        print("You win! 🎉")

    # Computer wins
    else:
        print("You lose! 😔")