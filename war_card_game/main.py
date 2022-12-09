import random
import arts as art

# card options
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


def replay():

    res = input(
        "Do you want to play again? Enter 'Y' for Yes or 'N' for No: ").lower()

    if res == 'y':
        game_play()
    else:
        print('GAME OVER, Hope you had fun')
        print(art.over)
# ******************************************************************************************

#  card classs creates a card


class Card:

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
 # takes in the  rank and returns the int value from the dictionary
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

# ******************************************************************************************

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

# ******************************************************************************************


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


print(art.logo)
print(art.card)


def game_play():

    player_one = Player("one")
    player_two = Player("two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    game_on = True
    round_num = 0

    while game_on:

        round_num += 1
        # print(f"Round {round_num}")

        if len(player_one.all_cards) == 0:
            print("Player One, out of cards!")
            print(art.two)
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two, out of cards!")
            print(art.one)
            game_on = False
            break

        # STAER A NEW ROUND
        # Otherwise, the game is still on!

        # Start a new round and reset current cards "on the table"
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                # Player One gets the cards
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            # Player Two Has higher Card
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # Player Two gets the cards
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                # No Longer at "war" , time for next round
                at_war = False

            else:
                # print('WAR!')
                # This occurs when the cards are equal.
                # We'll grab another card each and continue the current war.

                # First check to see if player has enough cards

                # Check to see if a player is out of cards:
                if len(player_one.all_cards) < 3:
                    print("Player One unable to play war! Game Over at War")
                    print(art.two)
                    game_on = False
                    break

                elif len(player_two.all_cards) < 3:
                    print("Player Two unable to play war! Game Over at War")
                    print(art.one)
                    game_on = False
                    break
                # Otherwise, we're still at war, so we'll add the next cards
                else:
                    for _ in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())
    replay()


game_play()
# ******************************************************************************************
