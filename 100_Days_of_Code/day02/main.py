# tip calculator
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# this function calculate the total tip given the total bill and percentage chosen
def tip_calculator(tip_percentage, bill):
    return bill * (tip_percentage / 100)

# this function calculate the total even split amongst the group


def split_bill(bill, tip_amount, num_of_people):
    return round((bill + tip_amount) / num_of_people, 2)

# this will ask the table if they would like to calculate split again using a different %


def replay():
    return input('Do you want to calculate tip again? Enter Yes or No: ').lower().startswith('y')


while True:
    print("Welcome to the tip calculator! \n")
    bill = float(input("What was the total bill? $ \n"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
    people = int(input("How many people to split the bill? \n"))

    tip_total = tip_calculator(tip, bill)
    final_split = split_bill(bill, tip_total, people)

    print(f"Each person should pay: ${final_split}")

    if not replay():
        break
