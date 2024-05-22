import random
import os
import time
import words_list
import shutil

def display_banner():
    banner = r"""
__        __            _   ____                           
\ \      / /__  _ __ __| | |  _ \ ___  ___  ___ _   _  ___ 
 \ \ /\ / / _ \| '__/ _` | | |_) / _ \/ __|/ __| | | |/ _ \
  \ V  V / (_) | | | (_| | |  _ <  __/\__ \ (__| |_| |  __/
   \_/\_/ \___/|_|  \__,_| |_| \_\___||___/\___|\__,_|\___|
   """
    terminal_width = shutil.get_terminal_size().columns
    banner_lines = banner.split('\n')
    centered_banner = '\n'.join(line.center(terminal_width) for line in banner_lines)
    print(centered_banner)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def centered_input(prompt, color_code=""):
    terminal_width = shutil.get_terminal_size().columns
    centered_prompt = prompt.center(terminal_width)
    print(color_code + centered_prompt + "\033[0m", end='', flush=True)
    user_input = input()
    return user_input.strip()

def centered_print(text, color_code=""):
    terminal_width = shutil.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(color_code + centered_text + "\033[0m")

def display_rules():
    title = "Rules"
    underline = "-" * len(title)
    rules = [
        "1. You need to guess the word by suggesting letters within a certain number of guesses.",
        "2. If the suggested letter is in the word, it is revealed in its correct positions.",
        "3. If the suggested letter is not in the word, you lose an attempt.",
        "4. The game continues until you either guess the word or run out of attempts."
    ]
    centered_print(title)
    centered_print(underline)
    for rule in rules:
        centered_print(rule)

def get_level():
    levels = {'1': 'easy', '2': 'medium', '3': 'hard'}
    while True:
        level = centered_input("Choose a level: 1. Easy  2. Medium  3. Hard: \n")
        if level in levels:
            return levels[level]
        else:
            centered_print("Invalid input. Please enter 1, 2, or 3.\n", "\033[91m")
            time.sleep(1)
            clear_screen()

def get_random_word(level):
    words = words_list.get_words()
    return random.choice(words[level])

def initialize_game_state(level):
    word = get_random_word(level).upper()
    hidden_word = ['_' for _ in word]
    attempts = 6 if level == 'easy' else 4 if level == 'medium' else 3
    guessed_letters = set()
    return word, hidden_word, attempts, guessed_letters

def display_current_state(hidden_word, attempts_left, guessed_letters):
    green_text = "\033[92m"
    red_text = "\033[91m"
    reset_text = "\033[0m"
    centered_print(f"Current word: {' '.join(hidden_word)}")
    centered_print(f"Attempts left: {green_text}{attempts_left}{reset_text}")
    centered_print(f"Guessed letters: {red_text}{', '.join(sorted(guessed_letters))}{reset_text}" + "\n")

def update_hidden_word(word, hidden_word, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            hidden_word[i] = guess

def play_again():
    while True:
        response = centered_input("Do you want to play again? (yes/no): \n").lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        else:
            centered_print("Invalid input. Please enter 'yes' or 'no'.", "\033[91m")
            time.sleep(2)
            clear_screen()

def main():
    display_banner()
    terminal_width = shutil.get_terminal_size().columns
    
    welcome_text = "Welcome to Word Rescue game!"
    underline = '-' * len(welcome_text)
    
    centered_print(welcome_text)
    centered_print(underline)

    name = ""
    while not name:
        name = centered_input("Please enter your name: " + "\n")
        if not name:
            centered_print("Name cannot be empty. Please enter your name.", "\033[91m")
    clear_screen()         
    
    greeting = f"Hello, {name}"
    greeting_underline = '-' * len(greeting)
    
    centered_print(greeting)
    centered_print(greeting_underline)

    rules_shown = False

    while True:
        if not rules_shown:
            while True:
                read_rules = centered_input("Do you want to read the rules? (yes/no): \n").lower()
                if read_rules in ['yes', 'no']:
                    break
                else:
                    centered_print("Invalid input. Please enter 'yes' or 'no'.", "\033[91m")
                    
            clear_screen()

            if read_rules == 'yes':
                display_rules()
                centered_input("Press Enter to continue... ", "\033[38;2;253;253;150m")
        
            rules_shown = True
        
        clear_screen()
        level = get_level()
        word, hidden_word, attempts_left, guessed_letters = initialize_game_state(level)

        while True:
            clear_screen()
            display_current_state(hidden_word, attempts_left, guessed_letters)
            guess = centered_input("Guess a letter: ").upper()

            if len(guess) != 1 or not guess.isalpha():
                centered_print("Invalid input. Please guess a single letter.", "\033[91m")
                time.sleep(2)
                clear_screen()
                continue

            if guess in guessed_letters:
                centered_print("You've already guessed that letter. Try a different one.", "\033[91m")
                time.sleep(2)
                clear_screen()
                continue

            guessed_letters.add(guess)

            if guess in word:
                update_hidden_word(word, hidden_word, guess)
                if '_' not in hidden_word:
                    clear_screen()
                    centered_print("Congratulations! You've guessed the word!", "\033[92m\033[1m")
                    break
            else:
                attempts_left -= 1
                if attempts_left == 0:
                    clear_screen()
                    centered_print("Sorry, you've run out of attempts. \n", "\033[91m\033[1m")
                    centered_print(f"The word was: \033[92m\033[1m{word}\033[0m\n")
                    time.sleep(1)
                    break
                 
        if not play_again():
            clear_screen()
            custom_yellow = "\033[38;2;253;253;150m"
            bold_text = "\033[1m"
            reset_text = "\033[0m"
            centered_print(f"{bold_text}{custom_yellow}Thanks for playing! Goodbye.{reset_text}")
            break

if __name__ == "__main__":
    main()
