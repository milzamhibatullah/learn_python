
trying=0
selected=9
limit =5

while trying<limit:
    guess_number = input("Guess a number between 1 and 9: ")
    guess_number = int(guess_number)

    if guess_number==selected:
        print("Correct!")
    trying+=1

print('Game Ended')