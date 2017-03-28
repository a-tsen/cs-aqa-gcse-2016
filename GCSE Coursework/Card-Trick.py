# Refer to the following link: http://filestore.aqa.org.uk/resources/computing/AQA-85203-SNEA3.PDF

from Tkinter import *

"""
Process:
1. 21 shuffled cards are dealt face up into 3 piles ltr row by row. User asked to pick a card first time round.
2. User is asked which pile their card is in.
3. Cards collected pile by pile. The selected pile goes in the middle.
4. Steps 1-3 repeated 2 more times
5. The selected card will be in position 11 and the user asked if it is their chosen card.
"""

root = Tk()


def card_generator():  # generates randomised list of 21 different playing cards
    pass


def display_cards():  # deals 21 cards into 3 piles ltr ttb and displays them
    pass  # first time around user should be prompted to think of a card


def submit_pile_no():  # lets user submit pile number
    pass


def combine_piles():  # combines the 3 piles ensuring the user's choice is in the middle
    pass


def output_card():  # outputs the chosen card (the 11th of 21 cards)
    pass


def game_loop():  # game loop for a trick
    pass


root.mainloop()
