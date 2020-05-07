from poka import *

finished = False

while not finished:
    the_table = Table("Herr Forehead")
    game_start(the_table)
    while True:
        game_pre_flop(the_table)
        game_post_flop(the_table)
        break
    finished = True

print("Game over!")