import random

def hangman():
    # List of words to choose from
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

    # Select a random word from the list
    word = random.choice(words)

    # Create a list to store the guessed letters
    guessed_letters = []

    # Set the number of attempts
    attempts = 6

    # Game loop
    while True:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        print(display_word)

        # Prompt the user for a letter
        guess = input("Guess a letter: ").lower()

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        # Check if the player has won or lost
        if "_" not in display_word:
            print("Congratulations! You guessed the word correctly.")
            break
        elif attempts == 0:
            print("Game over! You ran out of attempts. The word was:", word)
            break

        # Display the number of attempts remaining
        print("Attempts remaining:", attempts)
        print()

# Start the game
hangman()