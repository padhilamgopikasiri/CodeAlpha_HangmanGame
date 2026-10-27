
import random

print("welcome to hangman game")

words = ["apple", "orange", "mango", "banana", "strawberry"]
secret_word = random.choice(words)
display = ["_"] * len(secret_word)

print("guess the word:", " ".join(display))

wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

while "_" in display and wrong_guesses < max_wrong_guesses:
    guess = input("guess a letter:").lower()

    if guess in guessed_letters:
        print("already guessed letter")
    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("correct guess")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess

        else:
            print("wrong guess")
            wrong_guesses += 1

    print(" ".join(display))

if "_" not in display:
    print("congratulations, you won!!")
else:
    print("game over")
    print("the correct word is", secret_word)
