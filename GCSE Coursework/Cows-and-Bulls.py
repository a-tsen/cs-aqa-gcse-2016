# Refer to the following link: http://filestore.aqa.org.uk/resources/computing/AQA-85203-SNEA2.PDF

from Tkinter import *
import random

heading = ("Courier", 18)
normal = ("Courier", 13)

frame_padx = 50
title_pady = 10
base_pad = 10
entry_color = "pale goldenrod"
key_info_color = "dodgerblue"
default_width = 10

guesses = 0
# global guesses  # guesses has to be able to be accessed and changed from anywhere in the program
root = Tk()


def shift(current, new):  # shifts between Frames
    current.grid_remove()
    new.grid()


def gen_number():  # generates the 4-digit number according to the rules of Cows & Bulls
    number = ""
    digits_list = range(10)
    for _ in range(4):  # _ used as a throwaway variable name
        rand_index = random.randrange(len(digits_list))
        number += str(digits_list.pop(rand_index))  # ensures that there are no duplicate digits
    return number


def validate(user_guess):  # makes sure that the user gives sensible input - may update
    try:  # makes sure input is of the right type
        user_guess.isnumeric()
    except ValueError:
        return False

    if len(user_guess) != 4:  # checks for correct length
        return False
    else:
        for index in range(3):  # makes sure the user doesn't submit a number with duplicate digits
            if user_guess.count(user_guess[index]) > 1:
                return False

    return True  # meets all validation requirements


def count_cows_bulls(answer, user_guess):  # counts the number of cows and bulls
    bull_count = 0
    cow_count = 0
    for index in range(4):
        if user_guess[index] in answer:  # digit entered by user present in answer
            if user_guess[index] == answer[index]:  # correct position - a bull
                bull_count += 1
            else:  # incorrect position - a cow
                cow_count += 1
    return bull_count, cow_count


def submit_guess():  # callback function for the submission button
    pass


def game_loop():  # loop for a single game - may require revision of the game layout
    answer = gen_number()
    pass


instruct = Frame(root)  # instructions menu
Label(instruct, text="How to Play", font=heading).grid(row=0, column=0, padx=frame_padx, pady=title_pady)
description = Text(instruct, font=normal, width=frame_padx, height=16, wrap=WORD)
instruction = open("cows-bulls-instructions.txt", "r")  # gets instructions from an external file
description.insert(END, instruction.read())
instruction.close()
description.grid(row=1, column=0, padx=base_pad, pady=base_pad)
Button(instruct, text="Return", font=normal, command=lambda: shift(instruct, start)).grid(row=2, column=0, pady=base_pad)  # returns to the start menu

"""
0: [Cows and Bulls SPAN=3]
1: [Number:] [INPUT] [BUTTON Submit]
2: [TEXT for alerts SPAN=3]
3: [BUTTON Quit Game] [] [BUTTON Return to Menu]
"""

game = Frame(root)  # game menu
Label(game, text="Cows and Bulls", font=heading).grid(row=0, column=0, columnspan=3, padx=frame_padx, pady=title_pady)
Label(game, text="Guess:", font=normal).grid(row=1, column=0, padx=base_pad, pady=base_pad)
guess_entry = Entry(game, font=normal, bg=entry_color, width=6)
guess_entry.grid(row=1, column=1, padx=base_pad, pady=base_pad)
Button(game, text="Submit", font=normal, command=submit_guess).grid(row=1, column=2, padx=base_pad, pady=base_pad)
#  ALERT box
#  Quit Game / New Game

start = Frame(root)  # start menu
start.grid()
Label(start, text="Cows and Bulls", font=heading).grid(row=0, column=0, padx=frame_padx, pady=title_pady)
#  Resume existing game?
#  New game button
#  How to Play button

root.mainloop()
