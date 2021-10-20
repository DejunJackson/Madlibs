from game_pkg.player import Player
from game_pkg.menu import main_menu, show_leaderboards
from game_pkg.stories import story_one

all_players = []
while True:
    # Ask how many players there are and names
    choice = main_menu()
    if choice == '1' or choice == 'start game':
        print("Welcome!")
        numOfPlayers = int(input("How many Players are there? "))
        current_players = {}
        # Ask each player for their random words
        for x in range(numOfPlayers):

            name, words = story_one(x)
            # Instantiates player object and checks to see if the same name is used as before
            player = Player(name, words)
            for past_player in all_players:
                if name == past_player.name:
                    player.score = past_player.score
                    input(
                        f'\nWelcome back {name}! Your score is {player.score}. Press Enter to continue.')
                    break

            current_players[name] = player
            all_players.insert(0, player)

        # Print the name of player and their answers
        for player in current_players:
            print("\nHere is", current_players[player].name + "'s story:")
            current_players[player].read_story()
            input("Press enter to continue.")

        # Each player votes
        for voter in current_players:
            i = 1
            for votee in current_players:
                print(f"\n{i}. {current_players[votee].name}")
                i += 1
            vote = input(
                f"\nHi {current_players[voter].name}. Enter the name of the person you want to vote for: ")
            current_players[vote].vote += 1

        # Votes are compared and winner is announced
        most_votes = []
        for player in current_players:
            most_votes.append(current_players[player])
        winner = most_votes[0]
        for player in most_votes:
            if player.vote > winner.vote:
                winner = player
        winner.score += 1
        print('\nYour winner is', winner.name + '!')

        # Ask if they want to play again
        input("\nPress enter to go back to main menu. ")

    elif choice == '2' or choice == 'leaderboards':
        show_leaderboards(all_players)

    elif choice == '3' or choice == 'exit':
        print("\nSee you later!")
        break

    else:
        print("\nInvalid input")
