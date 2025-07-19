print("Welcome to the quiz game!")

option = input("Type 'play' to start or 'quit' to exit: ").lower()

if option != "play":
    print("Thank You!")
    quit()

print("Great! Let's begin the quiz.")

score = 0
Q = "Who is known as the 'Father of the Nation' in India?"
print(Q)
ans = input("Ans: ")
if ans.lower() == "mahatma gandhi":
    print("Correct!")
    score += 100
else:
    print("Incorrect!")
print()

Q = "Water is made up of which two elements?"
print(Q)
ans = input("Ans: ")
if ans.lower() == "hydrogen and oxygen":
    print("Correct!")
    score += 500
else:
    print("Incorrect!")
print()

Q = "Which is the largest continent in the world?"
print(Q)
ans = input("Ans: ")
if ans.lower() == "asia":
    print("Correct!")
    score += 1000
else:
    print("Incorrect!")
print()

Q = "How many legs does a spider have?"
print(Q)
ans = input("Ans: ")
if ans == 8:
    print("Correct!")
    score += 2000
else:
    print("Incorrect!")
print()

Q = "What is the capital of India?"
print(Q)
ans = input("Ans: ")
if ans.lower() == "new delhi":
    print("Correct!")
    score += 5000
else:
    print("Incorrect!")
print()

print(f"Congratulations! Your final score is {score}.")