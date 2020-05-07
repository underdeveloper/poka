from poka import *

finished = False

while not finished:
    print("Who's dealing?")
    dealer_name = input("> ")
    print("")
    the_table = Table(dealer_name)
    game_start(the_table)
    while True:
        game_pre_flop(the_table)
        game_post_flop(the_table)
        break
    finished = True

print("Game over!")
