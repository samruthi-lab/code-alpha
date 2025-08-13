import random

# Predefined list of words
words = ["apple", "house", "water", "chair", "plant"]

# Pick a random word from the list
secret_word = random.choice(words)
guessed_letters = []  # letters guessed so far
wrong_guesses = 0
max_wrong = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(secret_word))  # Initial blanks

# Game loop
while wrong_guesses < max_wrong:
    guess = input("\nGuess a letter: ").strip().lower()  # FIX: removes spaces

    # Validate single letter input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one letter.")
        continue

    # If already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # If guess is correct
    if guess in secret_word:
        print("✅ Good guess!")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_wrong - wrong_guesses} tries left.")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check if player has won
    if "_" not in display_word:
        print("\n🎉 You guessed the word! You win!")
        break
else:
    print(f"\n💀 Game over! The word was '{secret_word}'.")

