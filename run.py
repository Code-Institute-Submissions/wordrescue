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

def main():
    display_banner()
    terminal_width = shutil.get_terminal_size().columns
    
    welcome_text = "Welcome to Word Rescue game!"
    underline = '-' * len(welcome_text)
    
    print(welcome_text.center(terminal_width))
    print(underline.center(terminal_width))

    name = centered_input("Please enter your name: " + "\n")
    clear_screen()
    
    greeting = f"Hello, {name}!"
    greeting_underline = '-' * len(greeting)
    
    print(greeting.center(terminal_width))
    print(greeting_underline.center(terminal_width))

if __name__ == "__main__":
    main()
