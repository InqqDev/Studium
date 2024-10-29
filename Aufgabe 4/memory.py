__author__ = "Chris"

import os

CARDS = ["✿", "❄", "★", "♥", "✉", "✂", "✖", "✈", "♫", "☀",
         "✿", "❄", "★", "♥", "✉", "✂", "✖", "✈", "♫", "☀"]  # Symbols


def get_cards():  # Helping function to return cards


    return CARDS


def create_grid(cards):  # Creates 4 lists with 5 elements
    """
    This function creates 4 "rows".
    Parameters:
        cards (uses the symbols)
    Returns:
        grid: is 4x5 list of the symbols
    """


    grid = []
    for j in range(4):
        x_list = []
        for x in range(5):
            x_list.append(cards[j * 5 + x])
        grid.append(x_list)
    return grid


def get_symbols(grid, pos1, pos2):  # shows A1 - E4 instead of symbols when 
                                    # not revealed
    """
    This function shows A1 - E4 instead of symbols when cards unrevealed.
    Parameters:
        grid:   4x5 list of the symbols
        pos1:   1st guess    
        pos2:   2nd guess
    Returns:
        a:  symbol on pos1
        b:  symbol on pos2
    """


    x1 = ord(pos1[0]) - 65
    y1 = int(pos1[1]) - 1
    x2 = ord(pos2[0]) - 65
    y2 = int(pos2[1]) - 1
    a = grid[y1][x1]
    b = grid[y2][x2]
    return a, b


def take_cards(grid, pos1, pos2):  # Picking cards and replacing with 
                                   # empty string
    """
    This function replaces the symbols with empty string when no longer needed
    Parameters:
        grid:   4x5 list of the symbols
        pos1:   1st guess
        pos2:   2nd guess
    Returns:
        grid:   updated 4x5 grid
    """


    a, b = get_symbols(grid, pos1, pos2)
    if a == b:
        x1 = ord(pos1[0]) - 65
        y1 = int(pos1[1]) - 1
        x2 = ord(pos2[0]) - 65
        y2 = int(pos2[1]) - 1
        grid[y1][x1] = "  "
        grid[y2][x2] = "  "
    return grid


def draw_grid(grid, pos1 = None, pos2 = None):  # Shows memory in console
    """
    This funtion shows the memory in the console for the user.
    Parameters:
        grid:   4x5 list of the symbols
        pos1:   None (if choosing no value, else 1st guess)
        pos2:   None (if choosing no value, else 2nd guess)
    Reurns:
        s (The whole grid, switching symbols with empty string included
           and showes symbols if pos1 and pos2 are included) 
    """

    os.system('cls')  # clears board

    if pos1 != None and pos2 != None:
        a, b = get_symbols(grid, pos1, pos2)

    for i in range(len(grid)):
        s = ""
        for j in range(len(grid[0])):
            if grid[i][j] != "  ":
                pos = chr(65 + j) + str(i + 1)
                if pos != pos1 and pos != pos2:
                    s += pos + " "
                elif pos == pos1:
                    s += a + "  "
                else: 
                    s += b + "  "
            else: 
                s += "   "
        print(s)


if __name__ == "__main__":  # Testcases
    grid = create_grid(CARDS)  # returns normal 5x4 list
    #create_grid(1337)  # TypeError
    #create_grid(cards)  # NameError
    print(get_symbols(grid, "A1", "B1"))  # shows ('✿', '❄')
    #print(get_symbols(grid, A1, B2))  # NameError
    #print(get_symbols(grid, 11, 22))  # TypeError
    print(take_cards(grid, "A1", "A3"))  # A1 and A3 are replaced with "  "
    print(take_cards(grid, "A1", "A2"))  # normal grid cause no pair found
    #print(take_cards(grid, A2, "A3"))  # NameError
    #draw_grid(grid, "A1")  # UnboundLocalError
    draw_grid(grid, "A1", "A2")  # shows grid with A1 and A2 revealed symbols
    draw_grid(grid)  # shows normal grid
    