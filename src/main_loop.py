from poka import *

finished = False

while not finished:
    print("Who's dealing?")
    dealer_name = input("> ")
    print("")
    the_table = Table(dealer_name)
    game_start(the_table)
    print("\nPress any key to continue.")
    input("")
    game_pre_flop(the_table)
    while True:
        game_post_flop(the_table)
        break
    finished = True

print("Game over!")
