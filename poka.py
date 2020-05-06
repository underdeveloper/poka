from random import randint as ri
from random import shuffle as sh

class Card:
    ''' Card'''
    def __init__(self, suit, rank):
        self.suit = suit # "s", "h", "c", "d"
        self.rank = rank # 1-15
    def display(self): 
        if self.rank == 11:
            displayed_rank = "J"
        elif self.rank == 12:
            displayed_rank = "Q"
        elif self.rank == 13:
            displayed_rank = "K"
        elif self.rank == 14:
            displayed_rank = "A"
        else:
            displayed_rank = str(self.rank)
        return (str(self.suit) + "/" + displayed_rank)

class Deck:
    def __init__(self):
        DIAMONDS = [Card("d", i) for i in range(1, 15)]
        CLUBS = [Card("c", i) for i in range(1, 15)]
        HEARTS = [Card("h", i) for i in range(1, 15)]
        SPADES = [Card("s", i) for i in range(1, 15)]
        self.cards = DIAMONDS + CLUBS + HEARTS + SPADES  # array [0..51] of Card

    def shuffle(self):
        sh(self.cards)

    def display_deck(self):
        for i in range(len(self.cards)):
            print(self.cards[i].display(), end=' ')
        print("")

class CardCollection:
    '''A collection of cards.'''

    def __init__(self, holder):
        self.HOLDER = holder # str : Name of the player who is holding the hand.
        self.cards = [] # array [0..4] of Card

    def __draw_single(self, some_deck): # some_deck : Deck
        self.cards.append(some_deck.cards[0])
        some_deck.cards.pop(0)
    
    def draw_cards(self, some_deck, amount):
        for i in range(amount):
            self.__draw_single(some_deck)
    
    def __sort_by_rank(self):
        card_amount = len(self.cards)
        if card_amount == 0:
            print(self.PLAYER + "'s hand is empty.")
        elif card_amount == 1:
            print(self.PLAYER + "'s hand only has one card.")
        else:
            for i in range(0, card_amount):
                idxmin = i
                for j in range(i, card_amount):
                    if self.cards[j].rank < self.cards[idxmin].rank:
                        idxmin = j
                temp = self.cards[i]
                self.cards[i] = self.cards[idxmin]
                self.cards[idxmin] = temp

class PlayerHand(CardCollection):
    def __init__(self, holder):
        super().__init__(holder)
        self.bet = 0

    def display_hand(self):
        print(self.HOLDER + "'s hand:", end=' ')
        __displayed = self
        for i in range(len(__displayed.cards)):
            if __displayed.cards[i].rank == 11:
                __displayed.cards[i].rank = "J"
            elif __displayed.cards[i].rank == 12:
                __displayed.cards[i].rank = "Q"
            elif __displayed.cards[i].rank == 13:
                __displayed.cards[i].rank = "K"
            elif __displayed.cards[i].rank == 14:
                __displayed.cards[i].rank = "A"
            else:
                __displayed.cards[i].rank = str(__displayed.cards[i].rank)
        for i in range(len(__displayed.cards)):
            print(__displayed.cards[i].display(), end=' ')
        print("")
    
    def raise_bet(self, money):
        print( self.HOLDER + " " + ("betting" if self.bet == 0 else "raising their bet by") + " " + str(money) + "." )
        self.bet += money
        print( self.HOLDER + "'s bet is now " + str(self.bet) + "." )

class DealerHand(CardCollection):
    def display_table(self):
        print("These are on the table:", end=' ')
        for i in range(len(self.cards)):
            print(self.cards[i].display(), end=' ')
        print("")
    pass




the_house = Deck()
the_house.shuffle()
the_house.display_deck()

dealio = DealerHAnd("Dealdev")

my_hand = PlayerHand("Undev")
your_hand = PlayerHand("Overdev")

print("Drawing cards for everyone.")

my_hand.draw_cards(the_house, 2)
my_hand.display_hand()
your_hand.draw_cards(the_house, 2)
your_hand.display_hand()

print("Flop.")
dealio.draw_cards(the_house, 3)
dealio.display_table()

# the_house.display_deck()

my_hand.raise_bet(1000)
your_hand.raise_bet(1300)

print("Turn.")
dealio.draw_cards(the_house, 1)
dealio.display_table()

my_hand.raise_bet(1000)

print("River.")
dealio.draw_cards(the_house, 1)
dealio.display_table()
