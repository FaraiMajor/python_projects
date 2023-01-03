

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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


def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
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
    print(balance, lines)


main()
