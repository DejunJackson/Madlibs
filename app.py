from game_pkg.player_class import Player
from game_pkg.menu import main_menu, show_leaderboards

all_players = []
while True:
    # Ask how many players there are and names
    choice = main_menu()
    if choice == '1' or choice == 'start game':
        print("Welcome!")
        numOfPlayers = int(input("How many Players are there? "))
        players = {}
        # Ask each player for their random words
        for x in range(numOfPlayers):

            name = input(f"Hello Player {x + 1}! What is your name? ")

            words = {}

            adjective, adjective2, adjective3 = input(
                f"Hi {name}, please name three adjectives, separate them by a space, then press enter. \n").split()

            place, place2 = input(
                "Now name two cities, states, or countries, separate them by a space, then press enter. \n").split()

            femaleName, maleName = input(
                "Now name a female first name then a male first name, separate them by a space, then press enter. \n").split()

            bodyPart, bodyPart2, bodyPart3, bodyPart4 = input(
                "Now name 4 body parts, separate them by a space, then press enter. \n").split()

            organ = input("Finally name an organ and press enter. \n")

            words.update(adjective=adjective, adjective2=adjective2, adjective3=adjective3, place=place, place2=place2, femaleName=femaleName,
                         maleName=maleName, bodyPart=bodyPart, bodyPart2=bodyPart2, bodyPart3=bodyPart3, bodyPart4=bodyPart4, organ=organ)

            # Instantiates player object and checks to see if the same name is used as before
            player = Player(name, words)
            for past_player in all_players:
                if name == past_player.name:
                    player.score = past_player.score
                    input(
                        f'\nWelcome back {name}! Your score is {player.score}. Press Enter to continue.')
                    break

            players[name] = player
            all_players.insert(0, player)

        # Print the name of player and their answers
        for player in players:
            print("\nHere is", players[player].name + "'s story:")
            players[player].read_story()
            input("Press enter to continue.")

        # Each player votes
        for voter in players:
            i = 1
            for votee in players:
                print(f"\n{i}. {players[votee].name}")
                i += 1
            vote = input(
                f"\nHi {players[voter].name}. Enter the name of the person you want to vote for: ")
            players[vote].vote += 1

        # Votes are compared and winner is announced
        most_votes = []
        for player in players:
            most_votes.append(players[player])
        most = most_votes[0]
        for player in most_votes:
            if player.vote > most.vote:
                most = player
        most.score += 1
        print('Your winner is', most.name)

        # Ask if they want to play again
        con = input("Go back to main menu? y or n: ").lower()
        if con == 'n':
            print('Thanks for playing! Bye!')
            break

    elif choice == '2' or choice == 'leaderboards':
        show_leaderboards(all_players)

    elif choice == '3' or choice == 'exit':
        print("\nSee you later!")
        break

    else:
        print("Invalid input")
