import random

print(""" Welcome to <THE GUESSER> a game where you need to: \n
          guess the number generated by the computer, \n
          at the same time trying to beat your friends,\n
          and take the TOP Spot on the leaderboard.
          GOOD LUCK PLAYERS
          """)
players_num = int(input("Enter The Number of Players who are going to play here"))

players_names = []
players_scores = []

for player in range(0, players_num):
    player_name = input("Enter Player {} name here : ".format(player))
    players_names.append(player_name)

while True:
    players_records = {}
    guess_num = random.randint(0, 10)
    player_data = {}
    for player_no in players_names:
        print("\n Player {} its your turn to guess the number.".format(player_no))
        player_guess = int(input("Player {}, Enter your guess here : ".format(player_no)))
        players_records[player_no] = player_guess
        
    for player_rec in players_records:
        if players_records[player_rec] == guess_num:
            players_scores.append(1)
            print(" \n [+] Guess was correct [+] ")
        else:
            players_scores.append(-1)
            print("\n Incorrect Guess :( Better luck next time")
        for name in players_names:
            for score in players_scores:
                player_data[name] = len(players_scores)
        print(" \n CURRENT SCORES ARE : ", player_data)

# FOR NOW WE END HERE, I WILL KEEP UPDATING THIS CODE FROM TIME TO TIME AND WE'LL SEE WHERE WE GET TO 
# FEEL FREE TO PRATICE OR REVIEW IT


#Tech_To_The_World


#COPYRIGHT (c) : KUFRASHE TECHNOLOGIES 2018-2024
