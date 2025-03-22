import random

def guess_number():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    print("🎯 Welcome to the Guess the Number Game!")
    print("🔢 I have selected a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Run the game
guess_number()
