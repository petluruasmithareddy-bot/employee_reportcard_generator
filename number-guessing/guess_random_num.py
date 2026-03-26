import random

# Generate a random number between 1 and 10
secret_asmi = random.randint(1, 10)

print("🎯 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")

attempts = 3

while attempts > 0:
    guess = int(input("Enter your guess: "))
    

    if guess < secret_asmi:
        print("Too low! Try again.")
    
    elif guess > secret_asmi:
        print("Too high! Try again.")
    
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
    attempts -= 1

if attempts==0:
        print("gameover!")