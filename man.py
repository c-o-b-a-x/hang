import random

def prompt(*valid):
    ''' This function handles prompting the user to play a game '''
    while True:
        choice = input("Do you want to play a game? (yes/y or no/n): ").lower().strip()
        if choice in valid:
            if choice in ["yes", "y"]:
                print("Let's play a game!")
                return True 
            elif choice in ["no", "n"]:
                print("LAME!")
                return False 
        print("That isn't a valid choice. Please enter yes/y or no/n.")

def get_status(guess_count):
    """ Returns the current hangman status based on the guess count """
    statuses = [
        """
          _______
         |/      |
         |
         |
         |
         |
         |
       _|___
        """,
        """ 
          _______
         |/      |
         |      (_)
         |
         |
         |
         |
       _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |       |
         |       |
         |
         |
       _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|
         |       |
         |
         |
       _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |
         |
       _|___
        """,
        """
           _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      /
         |
       _|___
        """,
        """
          _______
         |/      |
         |      (_)
         |      \|/
         |       |
         |      / \\
         |
       _|___
        """
    ]
    return statuses[guess_count] if guess_count < len(statuses) else statuses[-1]

def guess_system(word):
    """ Handles the guess system """
    guess_count = 0
    guessed_letters = set()
    incorrect_guesses = []  
    word_display = ['_'] * len(word) 

    print(get_status(guess_count))  

    while guess_count < 6:
        print("Current word: " + ' '.join(word_display))
        print("Incorrect guesses: " + ', '.join(incorrect_guesses) if incorrect_guesses else "No incorrect guesses yet.")
        
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("THAT'S TOO MANY LETTERS")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"{guess} is in the word!")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            print(f"nope {guess} is not in the word")
            incorrect_guesses.append(guess) 
            guess_count += 1

        print(get_status(guess_count))

        if '_' not in word_display: 
            print("Congratulations! You've guessed the word:", ''.join(word_display))
            return

    print("Game Over! You've run out of guesses. The word was:", word)

def play_game():
    """ This function controls everything needed for the game to properly work """
    words = {"eminem", "superman", "cheer", "hunting", "mountain", "crush", "vaquero", "hangman", "aqueous", "dysprosium"}
    word = random.choice(list(words))

    print(f"The word has been selected. It has {len(word)} letters.")
    if prompt("yes", "y", "no", "n"):
        guess_system(word)

if __name__ == '__main__':
    play_game()
