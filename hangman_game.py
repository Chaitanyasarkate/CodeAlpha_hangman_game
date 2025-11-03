import random


# List of predefined words
words = ["python", "computer", "hangman", "program", "developer"]


# Choose a random word from the list
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
attempts_left = 6
guessed_letters = []

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 incorrect attempts allowed.\n")

# Game loop
while attempts_left > 0 and "_" in guessed_word:
    print("Word: ", " ".join(guessed_word))
    print(f"Attempts left: {attempts_left}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word_to_guess:
        print("✅ Good job! That letter is in the word.\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1
        print("❌ Wrong guess! Try again.\n")

# Check game result
if "_" not in guessed_word:
    print(f"🎉 Congratulations! You guessed the word: {word_to_guess}")
else:
    print(f"😢 Game Over! The word was: {word_to_guess}")


