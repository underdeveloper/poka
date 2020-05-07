from random import shuffle as sh

class Card:
    ''' A single card. '''

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
            displayed_rank = str(self.rank) if self.rank < 10 else "0"
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
        for _ in range(amount):
            self.__draw_single(some_deck)
    
    def __sort_by_rank(self):
        card_amount = len(self.cards)
        if card_amount == 0:
            print(self.HOLDER + "'s hand is empty.")
        elif card_amount == 1:
            print(self.HOLDER + "'s hand only has one card.")
        else:
            for i in range(0, card_amount):
                idxmin = i
                for j in range(i, card_amount):
                    if self.cards[j].rank < self.cards[idxmin].rank:
                        idxmin = j
                temp = self.cards[i]
                self.cards[i] = self.cards[idxmin]
                self.cards[idxmin] = temp

class HandPlayer(CardCollection):
    def __init__(self, holder):
        super().__init__(holder)
        self.bet = 0

    def display_hand(self):
        print(self.HOLDER + "'s hand:", end=' ')
        for i in range(len(self.cards)):
            print(self.cards[i].display(), end=' ')
        print("")
    
    def raise_bet(self, money):
        print( self.HOLDER + " " + ("betting" if self.bet == 0 else "raising their bet by") + " " + str(money) + "." )
        self.bet += money
        print( self.HOLDER + "'s bet is now " + str(self.bet) + "." )

class HandDealer(CardCollection):
    def display_table(self):
        print("These are on the table:", end=' ')
        for i in range(len(self.cards)):
            print(self.cards[i].display(), end=' ')
        print("")

class Table():
    def __init__(self, dealer_name):
        self.deck = Deck()
        self.dealer =  HandDealer(dealer_name)
        self.players = [self.dealer] # : array [0..9] of HandPlayer()
        self.player_seats = ["The Button", "Small Blind", "Big Blind", "Under the Gun", "Under the Gun Plus One", "Under the Gun Plus Two", "Middle Position", "Second Middle Position" "The Hijack", "The Cutoff"]
        self.player_abbv = ["btn", "sb", "bb", "utg", "utg+1", "utg+2", "mp", "mp2", "co", "hj"]
    def register_player(self, player_name):
        self.players.append(HandPlayer(player_name))
    def show_players(self):
        for i in range(1, len(self.players)):
            print("[Seat " + str(i) + "] " + self.player_seats[i] + ": " + self.players[i].HOLDER)
        print("[Dealer] The Button: " + self.dealer.HOLDER)
    def flop(self):
        self.dealer.draw_cards(deck, 3)
    def turn(self):
        self.dealer.draw_cards(deck, 1)
    def river(self):
        self.dealer.draw_cards(deck, 1)

def game_start(table):

    print("Welcome to Poka.py. This is just a game of Hold'em.")

    print("We begin by entering our names. Please enter Player 1's name.")
    this_player = input("> ")
    table.register_player(this_player)

    print("Player 1 \"" + this_player + "\" added as Small Blind.")
    print("Please enter Player 2's name.")
    this_player = input("> ")
    table.register_player(this_player)

    print("Player 2 \"" + this_player + "\" added as Big Blind.")
    print("Would you like to add more players? [Y/N]")
    while True:
        yn = input("> ").upper()
        if yn in ["Y", "N"]:
            break
        else:
            print("Invalid input, please try again.")
    if yn == "Y":
        player_count = 3
        while True:
            print("Please enter Player " + str(player_count) + "'s name.")
            this_player = input("> ")
            table.register_player(this_player)
            print("Player " + str(player_count) + " \"" + this_player + "\" added as " + table.player_seats[player_count] + ".")
            player_count += 1
            print("Would you like to add more players? [Y/N]")
            if player_count == 10:
                print("That's the maximum amount of players.")
                break
            while True:
                yn = input("> ").upper()
                if yn in ["Y", "N"]:
                    break
                else:
                    print("Invalid input, please try again.")
            if yn == "N":
                break
    print("All done.")
    print("Here are the players.")
    table.show_players()

def game_pre_flop(table):
    return

def game_post_flop(table):
    return
