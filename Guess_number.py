# Guess the number between 1 to 100 correctly
# https://roadmap.sh/projects/number-guessing-game

import random
print("\nWelcome to the Number Guessing Game! \n")

print("I'm thinking of a number between 1 and 100.\n")
num = random.randint(1, 100)
#print("\nRandom number generated is: ", num)

difficulty = int(input('''Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances): 

Enter your choice: '''))

chance = 0
if difficulty == 1:
    chance = 10
    print("\nYou have 10 chances to guess the correct number.")
elif difficulty == 2:
    chance = 5
    print("\nYou have 5 chances to guess the correct number.")
else:
    chance = 3
    print("\nYou have 3 chances to guess the correct number.")
    
print("\nLet's start the game!")

attempt = 0
while chance != 0:
    guess = int(input("Enter your guess: "))
    attempt += 1
    if guess == num:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
        print(f"The number generated was: {num}, good guess!")
        break
    elif guess > num:
        print(f"Incorrect! The number is less than {guess}.")
    else:
        print(f"Incorrect! The number is greater than {guess}.")
    chance -= 1    
    
print(f"The number generated was: {num}")        
        
