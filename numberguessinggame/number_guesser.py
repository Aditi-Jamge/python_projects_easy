import random

try:
    top_range = int(input("Enter a top range number: "))
    if top_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
except ValueError:
    print("Invalid Input!")
    quit()

random_number = random.randint(0,top_range)

guesses = 0
while True:
        guesses += 1

        try:
            guess_number = int(input("Guess a number: "))
            if guess_number <= 0:
                print("Your guess must be greater than 0.")
            elif guess_number > random_number:
                print("You were above the number!")
            elif guess_number < random_number:
                print("You were below the number!")
            else:
                print("Congrats! You got it!")
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

print(f"You got it in {guesses} guess(es).")