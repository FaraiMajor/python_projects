import random
import arts as art

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

playing = True

# ******************************************************************************************


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# ******************************************************************************************


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
# ******************************************************************************************


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
# ******************************************************************************************


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
# ******************************************************************************************


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Bet cannot be more than chips available")
            else:
                break

# ******************************************************************************************


def hit(deck, hand):

    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()

# ******************************************************************************************


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Enter 'h' for HIT or 's' for STAND\n")
        if x[0] == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

# ******************************************************************************************


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

# ******************************************************************************************


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# ******************************************************************************************


def player_busts(player, dealer, chips):
    print("Player busts!")
    print(art.dealer)
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print(f'\n{art.player}')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    print(art.player)
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print(f'\n{art.dealer}')
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


# ******************************************************************************************
print(art.logo)
while True:
    # Print an opening statement

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_cards = Hand()
    dealer_cards = Hand()
    for _ in range(2):
        player_cards.add_card(deck.deal_one())
        dealer_cards.add_card(deck.deal_one())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_cards, dealer_cards)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_cards)

        # Show cards (but keep one dealer card hidden)
        show_some(player_cards, dealer_cards)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_cards.value > 21:
            player_busts(player_cards, dealer_cards, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_cards.value <= 21:

        while dealer_cards.value < 17:
            hit(deck, dealer_cards)

        # Show all cards
        show_all(player_cards, dealer_cards)

        # Run different winning scenarios
        if dealer_cards.value > 21:
            dealer_busts(player_cards, dealer_cards, player_chips)
        elif dealer_cards.value > player_cards.value:
            dealer_wins(player_cards, dealer_cards, player_chips)
        elif dealer_cards.value < player_cards.value:
            player_wins(player_cards, dealer_cards, player_chips)
        else:
            push(player_cards, dealer_cards)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input(
        "Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print(art.over)
        break


# ******************************************************************************************
