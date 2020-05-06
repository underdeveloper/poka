from random import randint as ri
from random import shuffle as sh

class Card():
    def __init__(self, suit, number):
        self.suit = suit # "s", "h", "c", "d"
        self.number = number # 1-15
    def display(self):
        return ( str(self.suit) + "/" + str(self.number) )

DIAMONDS = [Card("d", i) for i in range(1, 16)]
CLUBS = [Card("c", i) for i in range(1, 16)]
HEARTS = [Card("h", i) for i in range(1, 16)]
SPADES = [Card("s", i) for i in range(1, 16)]

class Deck():
    def __init__(self):
        DIAMONDS = [Card("d", i) for i in range(1, 16)]
        CLUBS = [Card("c", i) for i in range(1, 16)]
        HEARTS = [Card("h", i) for i in range(1, 16)]
        SPADES = [Card("s", i) for i in range(1, 16)]
        self.cards = DIAMONDS + CLUBS + HEARTS + SPADES  # array [0..51] of Card

    def shuffle(self):
        sh(self.cards)

    def display_deck(self):
        for i in range(len(self.cards)):
            print(self.cards[i].display(), end=' ')
        print("")

class Hand():
    def __init__(self):
        self.cards = [] # array [0..4] of Card

    def draw(self, some_deck): # some_deck : Deck
        some_card = ri(0, len(some_deck.cards))
        self.cards.append(some_deck.cards[some_card])
        some_deck.cards.pop(some_card)
    
    def display_hand(self):
        for i in range(len(self.cards)):
            self.cards[i].display()


the_house = Deck()
the_house.shuffle()
the_house.display_deck()

my_hand = Hand()
my_hand.draw(the_house)
my_hand.display_hand()
