import random

# card options
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

#  card classs creates a card


class Card:

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
 # takes in the  rank and returns the int value from the dictionary
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Create a deck of 52 cards and enable shuffling and dealing


class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined! PS this is not inheritence or polymorphism
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Pop to remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # war game when u win war you get a list of card. use extend to add to your cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return (f'Player {self.name} has {len(self.all_cards)}.')


# ******************************************************************************************
# Test cases
deck = Deck()
deck.shuffle()
new = Player("Jose")
for dek in deck.all_cards:
    new.all_cards.append(dek)
print(new)
for dick in new.all_cards:
    print(dick)
remove = new.remove_one()
print(f'Card \"{remove}\" was removed')
print(new)
