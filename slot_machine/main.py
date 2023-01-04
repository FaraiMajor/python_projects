import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# we have 4 symbols in the slot and here we assign quantity for each symbol so A is most valuable
symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}


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


def main():
    balance = deposit()
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


main()
