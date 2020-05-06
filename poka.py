from random import randint as ri
from random import shuffle as sh

class Card():
    ''' Card'''
    def __init__(self, suit, number):
        self.suit = suit # "s", "h", "c", "d"
        self.number = number # 1-15
    def display(self):
        return ( str(self.suit) + "/" + str(self.number) )

class Deck():
    def __init__(self):
        DIAMONDS = [Card("d", i) for i in range(1, 15)]
        CLUBS = [Card("c", i) for i in range(1, 15)]
        HEARTS = [Card("h", i) for i in range(1, 15)]
        SPADES = [Card("s", i) for i in range(1, 15)]
        self.cards = DIAMONDS + CLUBS + HEARTS + SPADES  # array [0..51] of Card

    def shuffle(self):
        sh(self.cards)

    def display_deck(self):
        __displayed = self
        for i in range(len(__displayed.cards)):
            if __displayed.cards[i].number == 11:
                __displayed.cards[i].number = "J"
            elif __displayed.cards[i].number == 12:
                __displayed.cards[i].number = "Q"
            elif __displayed.cards[i].number == 13:
                __displayed.cards[i].number = "K"
            elif __displayed.cards[i].number == 14:
                __displayed.cards[i].number = "A"
            else:
                __displayed.cards[i].number = str(__displayed.cards[i].number)
        for i in range(len(__displayed.cards)):
            print(__displayed.cards[i].display(), end=' ')
        print("")

class Hand():
    '''A player. Has a collection of cars'''

    def __init__(self, player):
        self.PLAYER = player # str : Name of the player who is holding the hand.
        self.cards = [] # array [0..4] of Card

    def draw(self, some_deck): # some_deck : Deck
        some_card = ri(0, len(some_deck.cards)-1)
        self.cards.append(some_deck.cards[some_card])
        some_deck.cards.pop(some_card)
    
    def display_hand(self):
        print(self.PLAYER + "'s hand:", end=' ')
        __displayed = self
        for i in range(len(__displayed.cards)):
            if __displayed.cards[i].number == 11:
                __displayed.cards[i].number = "J"
            elif __displayed.cards[i].number == 12:
                __displayed.cards[i].number = "Q"
            elif __displayed.cards[i].number == 13:
                __displayed.cards[i].number = "K"
            elif __displayed.cards[i].number == 14:
                __displayed.cards[i].number = "A"
            else:
                __displayed.cards[i].number = str(__displayed.cards[i].number)
        for i in range(len(__displayed.cards)):
            print(__displayed.cards[i].display(), end=' ')
        print("")
    
    # def sort_by_number(self)


the_house = Deck()
# the_house.shuffle()
the_house.display_deck()

my_hand = Hand("Undev")
print("Drawing a card.")
my_hand.draw(the_house)
my_hand.display_hand()