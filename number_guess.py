import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please guess a number between 1 and 100.")
            elif guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def main():
    while True:
        play_game()
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != 'y':
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
