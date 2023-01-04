import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# we have 4 symbols in the slot and here we assign quantity for each symbol so A is most valuable
symbol_count = {
    "\U0001F351": 3,
    "\U0001F34E": 4,
    "\U0001F34F": 6,
    "\U0001F34B": 8
}
symbol_value = {
    "\U0001F351": 5,
    "\U0001F34E": 4,
    "\U0001F34F": 3,
    "\U0001F34B": 2
}

# ----------------------------------------------------------------------------------------------


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        """column[0][line] is so we always start on the first item and check the entire row"""
        symbol = columns[0][line]
        for column in columns:
            # check symbols in the column based on the row we are on
            sysmbol_to_check = column[line]
            if symbol != sysmbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
    # ----------------------------------------------------------------------------------------------


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    # nested loop to add symbols the same amount as given in the dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # insert into column not rows hence why we did not use [[1,2,3]] etc
    """
    1. create columns list to store a lists of single column
    -goal here is to have symbols on colums like a slot so we will have 3 column in this manner
    -columns = [[],[],[]]
    2.loop with a range of columns we assigned and create a column list to store the symbol for eachb column
    -while here make a copy of the sysmbols list to ensure that we loop through the symbols 3 times for 3 column
    -How it works is we loop again (nested) for rows(reels) and we append a random sysmbol to our column list
    -We then delete that symbol so that we dont select it again or no more than the symbols available
    -Now this is where the cooy comes into play
    -Copy list is what we will use to get a random value, delete it and not change out main symbols list
    -This ensure that we can do the other 2 columns
    3 after this we then ass that colomn list to our columns list
    - in the end we then have a list of lists like this columns = [[],[],[]]
    """
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# ----------------------------------------------------------------------------------------------


"""
exaplanation for printing slot machine function
Use Matrix transpose to convert our list into rows. As is right now our reel looks like this:
columns = [[a,a,a]                                                     [[a,b,c]
           [b,b,b]                                                     [a,b,c]
           [c,c,c]] but we want the first list to represent a column   [a,b,c]]
now each list is in a column and the reel in rows
"""


def print_slot_machine(columns):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(len(columns)):
        for col in range(len(columns[0])):
            result[col][row] = columns[row][col]

    for reels in result:
        print(reels[0], " | ", reels[1], " | ", reels[2])


# ----------------------------------------------------------------------------------------------

def deposit():
    """reponsible for collecting user input which will be their deposit"""
    while True:
        amount = input("How much would you like to deposit? $")
        # authenticate if the input is a digit
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# ----------------------------------------------------------------------------------------------


def get_lines():
    """slot machines always have lines(rows) os mixed art and column. this functions gets the lines"""
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{str(MAX_LINES)})?")
        # authenticate if the input is a digit
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines

#  player places their bet here

# ----------------------------------------------------------------------------------------------


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        # authenticate if the input is a digit
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# ----------------------------------------------------------------------------------------------


def spin(balance):

    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Insufficient funds in your account!!. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines}. Total bet is: ${total_bet}")

    slots = get_slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winnings_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ${balance}")
    print("\U0001F606")


main()
