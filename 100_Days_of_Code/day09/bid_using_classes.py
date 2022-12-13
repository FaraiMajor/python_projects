# define the auction class
class Auction:
    def __init__(self, items):
        self.items = items
        self.current_bid = 0
        self.current_bidder = None

    # function to start the auction
    def start_auction(self):
        # display the items up for auction
        print("Auction items:")
        for item in self.items:
            print(item)

        # start taking bids from bidders
        while True:
            bid = int(input("Enter your bid: "))

            # check if the bid is valid
            if bid > self.current_bid:
                self.current_bid = bid
                self.current_bidder = input("Enter your name: ")

            # check if the user wants to end the auction
            end = input("End auction? (Y/N) ")
            if end.lower() == "y":
                break

        # display the winning bid
        print("Winning bid: $%d" % self.current_bid)
        print("Winning bidder: %s" % self.current_bidder)


# create an instance of the auction
auction = Auction(["car", "boat", "house"])

# start the auction
auction.start_auction()
