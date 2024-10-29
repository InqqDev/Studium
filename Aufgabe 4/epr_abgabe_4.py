__author__ = "Chris"

import memory
from random import randint
from time import sleep


def no_cards_left(grid):  # Check if all cards revealed (if game over)
    """
    This function checks if the game is over.
    Parameters:
        grid:   4x5 list of symbols
    Returns:
        False:  if theres 1 element not revealed yet
        True:   if all elements got discovered (all elements are "  ") 
    """


    for sublist in grid:
        for elem in sublist:
            if elem != "  ":
                return False
    return True


def correct_input(grid, pos):  # Making sure code is robust
    """
    This function ensures if input is correct or not.
    Parameters:
        grid:   4x5 list of symbols
        pos:    position of a symbol   
    Returns:
        False (if 1st char of pos not a letter or 2nd char not a number
               or length of the pos is not 2 or pos is an already discovered
               card)
        True (Else)
    """


    letter = ['A', 'B', 'C', 'D', 'E']
    number = ['1', '2', '3', '4', '5']

    if not pos[0] in letter or not pos[1] in number:
        return False
    elif len(pos) != 2:
        return False
    elif pos in grid_empty_cards(grid):
        return False
    return True

def grid_empty_cards(grid):  # Shows if no cards left
    """
    This function returns all positions where all cards got discovered.
    Parameters:
        grid:   4x5 list of symbols
    Returns:
        l:  list of all positions of all cards that got discovered
    """


    l = []
    for i, lst in enumerate(grid):
        for j, elem in enumerate(lst):
            if elem == "  ":
                l.append(chr(65 + j) + str(i + 1))
    return l 

def memory_game():  # final memory game with inputs from user
    """
    This function is the final memory game with inputs from user.
    Parameters:
        None
    Returns:
        None
    """


    cards = memory.get_cards()
    shuffled = []
    print(cards)
    while cards != []:  # shuffles cards
        i = randint(0, len(cards) - 1)
        shuffled.append(cards.pop(i))
    print(shuffled)

    grid = memory.create_grid(shuffled)
    rounds = 0  # shows in how many rounds game was won

    while not no_cards_left(grid):  # loops until all pairs found
        memory.draw_grid(grid)  # shows current board
        while True:
            pos1 = input("Wähle die Position der ersten Karte," +  
                         "die du aufgedeckt haben willst: ")
            if correct_input(grid, pos1):
                break
            print("Kein korrekter Input")
        while True:
            pos2 = input("Wähle die Position der zweiten Karte," + 
                         "die du aufgedeckt haben willst: ")
            if correct_input(grid, pos2) and pos1 != pos2:
                break
            print("Kein korrekter Input!")

        memory.draw_grid(grid, pos1, pos2)
        sleep(3)  # shows both cards for 3 sec and hides them again
        memory.draw_grid(grid)
        grid = memory.take_cards(grid, pos1, pos2)
        rounds += 1

    print(f"Du hast {rounds} Runden gebraucht um alle Karten aufzudecken")

    play_again = input("Willst du erneut spielen (y/n)")

    if play_again == "y":
        memory_game()

memory_game()

###TESTCASES###
#   1. If u choose 2 same cards, the console shows
#      "Kein korrekter Input"
#   2. If you choose 2 cards that are not a pair, the symbols will be visible
#      for 3 sec and are replaced again.
#   3. If you choose as an input a string with 3 or more chars, the console
#      shows "Kein korrekter Input!"
#   4. If you choose a position of a card that has already been eliminated as
#      a pair, then the console shows "Kein korrekter Input!"
#   5. If the 1st char is not A, B, C, D, E or the 2nd char is not
#      a number between 1 - 4, then the console shows "Kein korrekter Input!"
