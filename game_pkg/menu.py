def main_menu():
    print()
    print("          === Multiplayer Madlibs ===          ")
    print()
    print("------------------------------------------")
    print("| 1. Start Game                          |")
    print("------------------------------------------")
    print("| 2. Leaderboards                        |")
    print("------------------------------------------")
    print("| 3. Exit                                |")
    print("------------------------------------------")
    choice = input("\nWhat would you like to do? ").lower()

    return choice


def show_leaderboards(players):
    leaderboards = []

    if len(players) == 0:
        print('\nThere are no scores to print at this time. Go play some games!')
    else:
        for player in players:
            dup = False
            duplicate = player
            for player_check in leaderboards:
                if duplicate.name == player_check.name:
                    dup = True
                    break

            if dup == False:
                leaderboards.append(duplicate)

    high_idx = len(leaderboards) - 1

    for i in range(high_idx):
        for j in range(high_idx):
            score = leaderboards[j].score
            next_score = leaderboards[j+1].score
            player = leaderboards[j]
            next_player = leaderboards[j+1]
            if score < next_score:
                leaderboards[j] = next_player
                leaderboards[j+1] = player

    for player in leaderboards:
        print(player.name, player.score)
