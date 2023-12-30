import random

def choose_word():
    words = ["hangman", "python", "programming", "code", "challenge", "openai"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print('Welcome to Hangman!','black')

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Current word: {current_display}")

        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                incorrect_guesses += 1
                guessed_letters.append(guess)

            if incorrect_guesses == max_incorrect_guesses:
                print(f"Sorry, you've reached the maximum number of incorrect guesses. The word was {word_to_guess}. Game over!")
                break

            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
