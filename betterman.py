import tkinter as tk
import random

# List of words to guess
WORDS = ["crush", "cheer", "challenge", "programming", "development","joy","celebrate"]

MAX_ATTEMPTS = 6

# ASCII Art stages for Hangman
HANGMAN_PICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

class HangmanGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hangman")

        # Dark theme colors
        self.bg_color = "#1e1e1e"      # Dark gray background
        self.fg_color = "#ffffff"      # White text
        self.error_color = "#ff6347"   # Red for wrong guesses
        self.success_color = "#32cd32" # Green for winning
        self.input_bg_color = "#333333" # Darker background for input
        self.input_fg_color = "#00ff00" # Green for text input

        # Set window background color
        self.root.configure(bg=self.bg_color)

        # Choose a random word
        self.word_to_guess = random.choice(WORDS)
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.incorrect_guesses = 0
        self.guessed_letters = []

        # Create UI elements
        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Arial", 24),
                                   bg=self.bg_color, fg=self.fg_color)
        self.word_label.pack(pady=20)

        self.message_label = tk.Label(self.root, text="Guess a letter or try the whole word!", font=("Arial", 14),
                                      bg=self.bg_color, fg=self.fg_color)
        self.message_label.pack(pady=10)

        self.ascii_label = tk.Label(self.root, text=HANGMAN_PICS[self.incorrect_guesses], font=("Courier", 12),
                                    bg=self.bg_color, fg=self.fg_color, justify=tk.LEFT)
        self.ascii_label.pack(pady=10)

        # Label for single letter guess
        self.letter_guess_label = tk.Label(self.root, text="Enter a letter:", font=("Arial", 14),
                                            bg=self.bg_color, fg=self.fg_color)
        self.letter_guess_label.pack(pady=5)

        # Input for single letter guesses
        self.input_entry = tk.Entry(self.root, font=("Arial", 14),
                                    bg=self.input_bg_color, fg=self.input_fg_color, insertbackground=self.input_fg_color)
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.handle_letter_guess)  # Enter key to submit single letter guess

        # Label for full word guess
        self.word_guess_label = tk.Label(self.root, text="Guess the whole word:", font=("Arial", 14),
                                          bg=self.bg_color, fg=self.fg_color)
        self.word_guess_label.pack(pady=5)

        # Input for guessing the entire word
        self.word_guess_entry = tk.Entry(self.root, font=("Arial", 14),
                                         bg=self.input_bg_color, fg=self.input_fg_color, insertbackground=self.input_fg_color)
        self.word_guess_entry.pack(pady=10)
        self.word_guess_entry.bind("<Return>", self.handle_word_guess)  # Enter key to submit whole word guess

        self.incorrect_label = tk.Label(self.root, text="Incorrect guesses: 0", font=("Arial", 14),
                                        bg=self.bg_color, fg=self.fg_color)
        self.incorrect_label.pack(pady=10)

        self.result_label = tk.Label(self.root, font=("Arial", 16), bg=self.bg_color)
        self.result_label.pack(pady=20)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=("Arial", 14),
                                        bg=self.input_bg_color, fg=self.input_fg_color, activebackground=self.bg_color,
                                        activeforeground=self.fg_color)
        self.restart_button.pack(pady=10)

        self.root.mainloop()

    def handle_letter_guess(self, event):
        guess = self.input_entry.get().lower()

        # Clear the input field
        self.input_entry.delete(0, tk.END)

        # Ignore guesses that are not single letters or already guessed
        if len(guess) != 1 or not guess.isalpha() or guess in self.guessed_letters:
            self.message_label.config(text="Invalid guess. Try again.")
            return

        self.guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in self.word_to_guess:
            self.message_label.config(text=f"Good guess: {guess}")
            for i, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.guessed_word[i] = guess
        else:
            self.incorrect_guesses += 1
            self.message_label.config(text=f"Wrong guess: {guess}")
            self.incorrect_label.config(text=f"Incorrect guesses: {self.incorrect_guesses}")

        # Update the displayed word and ASCII art
        self.word_label.config(text=" ".join(self.guessed_word))
        self.ascii_label.config(text=HANGMAN_PICS[self.incorrect_guesses])

        # Check if the game is over
        self.check_game_over()

    def handle_word_guess(self, event):
        guessed_word = self.word_guess_entry.get().lower()

        # Clear the input field
        self.word_guess_entry.delete(0, tk.END)

        if guessed_word == self.word_to_guess:
            self.message_label.config(text="Correct! You've guessed the word!", fg=self.success_color)
            self.word_label.config(text=" ".join(self.word_to_guess))
            self.result_label.config(text="You win! Well done!", fg=self.success_color)
            self.end_game()
        else:
            self.incorrect_guesses = MAX_ATTEMPTS  # Max out incorrect guesses if word guess is wrong
            self.message_label.config(text="Incorrect word guess! You lose.", fg=self.error_color)
            self.ascii_label.config(text=HANGMAN_PICS[-1])  # Show final stage of hangman
            self.result_label.config(text=f"You lose! The word was '{self.word_to_guess}'.", fg=self.error_color)
            self.end_game()

    def check_game_over(self):
        if "_" not in self.guessed_word:
            self.result_label.config(text="You win! Well done!", fg=self.success_color)
            self.end_game()
        elif self.incorrect_guesses >= MAX_ATTEMPTS:
            self.result_label.config(text=f"You lose! The word was '{self.word_to_guess}'.", fg=self.error_color)
            self.ascii_label.config(text=HANGMAN_PICS[-1])  # Final hangman drawing
            self.end_game()

    def end_game(self):
        # Disable input after the game ends
        self.input_entry.config(state=tk.DISABLED)
        self.word_guess_entry.config(state=tk.DISABLED)

    def restart_game(self):
        # Reset game state
        self.word_to_guess = random.choice(WORDS)
        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.incorrect_guesses = 0
        self.guessed_letters = []

        # Update the UI
        self.word_label.config(text=" ".join(self.guessed_word))
        self.message_label.config(text="Guess a letter or try the whole word!")
        self.incorrect_label.config(text="Incorrect guesses: 0")
        self.result_label.config(text="")
        self.ascii_label.config(text=HANGMAN_PICS[self.incorrect_guesses])

        # Re-enable input
        self.input_entry.config(state=tk.NORMAL)
        self.word_guess_entry.config(state=tk.NORMAL)

if __name__ == "__main__":
    HangmanGame()