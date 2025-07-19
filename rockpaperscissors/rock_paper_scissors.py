import random

user_wins = 0
computer_wins = 0
option = ["rock", "paper", "scissor"]

while True:
    user_input = input("Select from rock/paper/scissor or 'Q' for 'quit': ").lower()
    if user_input == "q":
        break

    elif user_input not in option:
        print("Please enter valid input!")
        continue
    
    random_input = random.randint(0,2)
    computer_input = option[random_input]
    print("Computer picked:", computer_input)

    if user_input == computer_input:
        print("It's a tie. Let's play again!\n")

    elif user_input == "rock" and computer_input == "scissor":
        print("Congrats, You won!\n")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print("Congrats, You won!\n")
        user_wins += 1
    elif user_input == "scissor" and computer_input == "paper":
        print("Congrats, You won!\n")
        user_wins += 1
    else:
        print("Oops! You lost the game.\n")
        computer_wins += 1

print(f"You won the game {user_wins} time(s).")
print(f"Computer Won {computer_wins} time(s).")
print("Thank you for playing!\nPlay again soon!\n")



















