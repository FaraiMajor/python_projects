# secret auction
import os
from art import logo
# Clearing the Screen

print(logo)
bids = {}


def start_auction():

    while True:
        name = input("What is your name? \n")
        price = int(input("what is your bid? \n$ "))
        bids[name] = price

        end_bid = input("Are there anymore bidders? (Y/N) ")
        if end_bid.lower() == "n":
            break
        else:
            os.system('clear')

    print(bids)
    highest_bid = 0

    for x in bids:
        if bids[x] > highest_bid:
            highest_bid = bids[x]
        # make a list of all values using values() function then get the index of the highest bid
    index = list(bids.values()).index(highest_bid)
    # put all the keys in a list and pass the index we found to return the key in that position
    bidder_name = list(bids.keys())[index]
    print(f'Highest bid is ${highest_bid} by {bidder_name}')


start_auction()
