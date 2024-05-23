import random
import os
import time
import words_list
import shutil

def get_terminal_width():
    return shutil.get_terminal_size().columns

def center_text(text: str) -> str:
    width = get_terminal_width()
    return text.center(width)

def display_banner():
    banner = r"""
__        __            _   ____                           
\ \      / /__  _ __ __| | |  _ \ ___  ___  ___ _   _  ___ 
 \ \ /\ / / _ \| '__/ _` | | |_) / _ \/ __|/ __| | | |/ _ \
  \ V  V / (_) | | | (_| | |  _ <  __/\__ \ (__| |_| |  __/
   \_/\_/ \___/|_|  \__,_| |_| \_\___||___/\___|\__,_|\___|
   """
    for line in banner.splitlines():
        print(center_text(line))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt: str) -> str:
    print(center_text(prompt), end='', flush=True)
    return input().strip()

def display_message(message: str):
    print(center_text(message))

def display_rules():
    title = "Rules"
    underline = "-" * len(title)
    rules = [
        "1. You need to guess the word by suggesting letters within a certain number of guesses.",
        "2. If the suggested letter is in the word, it is revealed in its correct positions.",
        "3. If the suggested letter is not in the word, you lose an attempt.",
        "4. The game continues until you either guess the word or run out of attempts."
    ]
    print(center_text(title))
    print(center_text(underline))
    for rule in rules:
        print(center_text(rule))

    yellow_text = "\033[93mPress Enter to continue...\033[0m"
    print(center_text(yellow_text))
    input()  # Wait for the user to press Enter

def get_level() -> str:
    levels = {'1': 'easy', '2': 'medium', '3': 'hard'}
    while True:
        level = get_input("Choose a level: 1. Easy  2. Medium  3. Hard: \n")
        if level in levels:
            return levels[level]
        else:
            display_message("Invalid input. Please enter 1, 2, or 3.\n")
            time.sleep(1)
            clear_screen()

def get_random_word(level: str) -> str:
    words = words_list.get_words()
    return random.choice(words[level])

def initialize_game_state(level: str) -> tuple:
    word = get_random_word(level).upper()
    hidden_word = ['_' for _ in word]
    attempts = 6 if level == 'easy' else 4 if level == 'medium' else 3
    guessed_letters = set()
    return word, hidden_word, attempts, guessed_letters

def display_current_state(hidden_word: list, attempts_left: int, guessed_letters: set):
    print(center_text(f"Current word: {' '.join(hidden_word)}"))
    green_attempts_left = f"\033[92m{attempts_left}\033[0m"
    print(center_text(f"Attempts left: {green_attempts_left}"))
    red_guessed_letters = ', '.join([f"\033[91m{letter}\033[0m" for letter in sorted(guessed_letters)])
    print(center_text(f"Guessed letters: {red_guessed_letters}"))

def update_hidden_word(word: str, hidden_word: list, guess: str):
    for i, letter in enumerate(word):
        if letter == guess:
            hidden_word[i] = guess

def play_again() -> bool:
    while True:
        response = get_input("Do you want to play again? (yes/no): \n").lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        else:
            display_message("Invalid input. Please enter 'yes' or 'no'.")
            time.sleep(2)
            clear_screen()

def main():
    display_banner()
    
    welcome_text = "Welcome to Word Rescue game!"
    underline = '-' * len(welcome_text)
    
    print(center_text(welcome_text))
    print(center_text(underline))

    name = ""
    while not name:
        name = get_input("Please enter your name: " + "\n")
        if not name:
            display_message("Name cannot be empty. Please enter your name.")
    clear_screen()         
    
    greeting = f"Hello, {name}"
    greeting_underline = '-' * len(greeting)
    
    print(center_text(greeting))
    print(center_text(greeting_underline))

    rules_shown = False

    while True:
        if not rules_shown:
            while True:
                read_rules = get_input("Do you want to read the rules? (yes/no): \n").lower()
                if read_rules in ['yes', 'no']:
                    break
                else:
                    display_message("Invalid input. Please enter 'yes' or 'no'.")
                    
            clear_screen()

            if read_rules == 'yes':
                display_rules()
        
            rules_shown = True
        
        clear_screen()
        level = get_level()
        word, hidden_word, attempts_left, guessed_letters = initialize_game_state(level)

        while True:
            clear_screen()
            display_current_state(hidden_word, attempts_left, guessed_letters)
            guess = get_input("Guess a letter: " + "\n").upper()

            if len(guess) != 1 or not guess.isalpha():
                display_message("Invalid input. Please guess a single letter.")
                time.sleep(2)
                clear_screen()
                continue

            if guess in guessed_letters:
                display_message("You've already guessed that letter. Try a different one.")
                time.sleep(2)
                clear_screen()
                continue

            guessed_letters.add(guess)

            if guess in word:
                update_hidden_word(word, hidden_word, guess)
                if '_' not in hidden_word:
                    clear_screen()
                    display_message("Congratulations! You've guessed the word!")
                    break
            else:
                attempts_left -= 1
                if attempts_left == 0:
                    clear_screen()
                    display_message("\033[91mSorry, you've run out of attempts.\033[0m")
                    display_message(f"The word was: \033[92m{word}\033[0m")
                    time.sleep(1)
                    break
                 
        if not play_again():
            clear_screen()
            display_message("\033[93mThanks for playing! Goodbye.\033[0m")
            break

if __name__ == "__main__":
    main()
