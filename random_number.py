import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Guess the number between 1 and 100")

while True:
    try:
        guess = int(input("👉 Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    attempts += 1

    if guess == number:
        print(f"✅ Correct! You guessed the number in {attempts} attempts.")
        break
    elif guess < number:
        print("📉 Too small! Try a bigger number.")
    else:
        print("📈 Too large! Try a smaller number.")
