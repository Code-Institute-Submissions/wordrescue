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

def display_rules():
    rules = [
        "1. You need to guess the word by suggesting letters within a certain number of guesses.",
        "2. If the suggested letter is in the word, it is revealed in its correct positions.",
        "3. If the suggested letter is not in the word, you lose an attempt.",
        "4. The game continues until you either guess the word or run out of attempts."
    ]
    for rule in rules:
        print(rule.center(shutil.get_terminal_size().columns))

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
            centered_input("\033[91mName cannot be empty. Please enter your name.\033[0m" + "\n")

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
                    centered_input("\033[91mInvalid input. Please enter 'yes' or 'no'.\033[0m" + "\n")
                    
            clear_screen()

            if read_rules == 'yes':
                display_rules()
                centered_input("\n\033[38;2;253;253;150mPress Enter to continue... \033[0m")
                input()
        
            rules_shown = True
        
        clear_screen()

if __name__ == "__main__":
    main()
