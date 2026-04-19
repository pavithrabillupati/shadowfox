import random

words = [
    ("python", "Programming language"),
    ("apple", "A fruit"),
    ("tiger", "A wild animal"),
    ("table", "Used for writing or eating"),
    ("phone", "Used for communication")
]

stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

word, hint = random.choice(words)
guessed = ["_"] * len(word)
used_letters = []
lives = len(stages) - 1

print("Welcome to Hangman!")
print("Hint:", hint)

while lives > 0 and "_" in guessed:
    print(stages[len(stages) - 1 - lives])
    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))
    
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("Already used!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        lives -= 1
        print("Wrong! Lives left:", lives)

print(stages[len(stages) - 1 - lives])

if "_" not in guessed:
    print("You win! The word was:", word)
else:
    print("You lose! The word was:", word)