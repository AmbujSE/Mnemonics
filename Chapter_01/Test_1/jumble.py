from tkinter import *
import math
#
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
#
# window = Tk()
# window.title()
# window.config(padx=50, pady=50, bg="green")
#
# title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"))
# title_label.grid(column=2, row=1)


#
# def count_down():
# #
# count = 3 * 60
# minute = math.floor(count / 60)
# second = count % 60
#
# while count > 0:
#     print(f"{minute}:{second:02}")
#     count -= 1
import time

import time
import os


def clear_terminal():
    # Clear terminal screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')


def countdown(total_seconds):
    for seconds in range(total_seconds, 0, -1):
        minutes, remaining_seconds = divmod(seconds, 60)
        print(f"\rTime remaining: {minutes:02}:{remaining_seconds:02}", end="")
        time.sleep(1)

    print("\rCountdown complete!")
    time.sleep(2)  # Wait for 2 seconds after countdown completion
    clear_terminal()


# Set the desired countdown duration in seconds
entered_words = []
# Start the countdown
while True:
    selected_time = int(input("How much Time do you need? (maximum: 3 minutes): "))
    if 1 <= selected_time <= 3:
        print("Memorize the list: ")
        with open("data.txt") as file:
            for line in file:
                print(line.rstrip())
        countdown_duration = 10
        countdown(countdown_duration)
        user_input = input("Enter the words: ")
        with open("entered_words.txt", "w") as en_file:
            en_file.write(f"{user_input}\n")
        break
    else:
        pass
