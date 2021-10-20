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
    elif len(players) == 1:
        print("------------------------------------------")
        print("|    Player                Score         |")
        print("------------------------------------------")
        print(
            f'\n     1.{players[0].name}                    {players[0].score}')
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

    for j in range(high_idx):
        score = leaderboards[j].score
        next_score = leaderboards[j+1].score
        player = leaderboards[j]
        next_player = leaderboards[j+1]

        if score < next_score:
            leaderboards[j] = next_player
            leaderboards[j+1] = player

    print("------------------------------------------")
    print("|    Player                Score         |")
    print("------------------------------------------")
    position = len(leaderboards) - 1
    for player in leaderboards:
        print(
            f'\n    {position}.{player.name}                      {player.score}')
        position += 1
