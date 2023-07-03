# ********** JetBrains Academy - Python for Beginners **********
# ******** Project - Last Pencil : Stage 3 / 5 ********
# ******** https://hyperskill.org/projects/258/stages/1304/implement ********

def play_round():
    pick = int(input(f"{list_players[round + index_first_player]}'s turn:\n"))
    return pick

nb_pencils = int(input("How many pencils would you like to use:\n"))
first_player = input("Who will be the first (Davy, Jones):\n")
list_players = ["Davy", "Jones"]
round = 0
index_first_player = list_players.index(first_player)
print('|' * nb_pencils)

while nb_pencils != 0:
    nb_pencils = nb_pencils - play_round()



