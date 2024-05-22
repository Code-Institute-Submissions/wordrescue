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
    print(title.center(shutil.get_terminal_size().columns))
    print(underline.center(shutil.get_terminal_size().columns))
    for rule in rules:
        print(rule.center(shutil.get_terminal_size().columns))

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
    print(f"Current word: {' '.join(hidden_word)}".center(shutil.get_terminal_size().columns))
    print(f"Attempts left: {green_text}{attempts_left}{reset_text}".center(shutil.get_terminal_size().columns))
    print(f"Guessed letters: {red_text}{', '.join(sorted(guessed_letters))}{reset_text}".center(shutil.get_terminal_size().columns))

def update_hidden_word(word, hidden_word, guess):
    for i, letter in enumerate(word):
        if letter == guess:
            hidden_word[i] = guess

def main():
    display_banner()
    terminal_width = shutil.get_terminal_size().columns
    
    welcome_text = "Welcome to Word Rescue game!"
    underline = '-' * len(welcome_text)
    
    print(welcome_text.center(terminal_width))
    print(underline.center(terminal_width))

    name = ""
    while not name:
        name = centered_input("Please enter your name: " + "\n")
        if not name:
            centered_print("Name cannot be empty. Please enter your name.\n", "\033[91m")
    clear_screen()         
    
    greeting = f"Hello, {name}"
    greeting_underline = '-' * len(greeting)
    
    print(greeting.center(terminal_width))
    print(greeting_underline.center(terminal_width))

    rules_shown = False

    while True:
        if not rules_shown:
            while True:
                read_rules = centered_input("Do you want to read the rules? (yes/no): " + "\n").lower()
                if read_rules in ['yes', 'no']:
                    break
                else:
                    centered_print("Invalid input. Please enter 'yes' or 'no'.\n", "\033[91m")
                    
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
                print("\033[91mInvalid input. Please guess a single letter.\033[0m")
                time.sleep(2)
                clear_screen()
                continue

            if guess in guessed_letters:
                print("\033[91mYou've already guessed that letter. Try a different one.\033[0m")
                time.sleep(2)
                clear_screen()
                continue

            guessed_letters.add(guess)

            if guess in word:
                update_hidden_word(word, hidden_word, guess)
                if '_' not in hidden_word:
                    clear_screen()
                    print("\033[92m\033[1mCongratulations! You've guessed the word!\033[0m")
                    time.sleep(2)
                    break
            else:
                attempts_left -= 1
                if attempts_left == 0:
                    clear_screen()
                    print("\033[91m\033[1mSorry, you've run out of attempts.\033[0m\n")
                    print(f"The word was: \033[92m\033[1m{word}\033[0m\n")
                    time.sleep(2)
                    break
        

if __name__ == "__main__":
    main()
