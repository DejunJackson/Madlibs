"""This module is the main game loop"""
from game_pkg.player import Player
from game_pkg.menu import main_menu
from game_pkg.stories import story
from game_pkg.database import add_to_database, update_all_players, show_leaderboards
from game_pkg.validation import validate_name, validate_vote


while True:
    all_players = []

    # appends all the players from the database to the all_players list for each game
    update_all_players(all_players)
    choice = main_menu()
    if choice == '1' or choice == 'start game':
        print("\nWelcome!")
        numOfPlayers = int(input("\nHow many Players are there? "))
        current_players = {}

        # Ask each player for their random words
        for x in range(numOfPlayers):

            # Makes sure name entered is between 2 and 10 characters
            name = validate_name(x)

            words = {}

            # if a player uses same name as in database, it uses the player from db in the current game
            found = False
            for past_player in all_players:
                if name == past_player.name:
                    player = past_player
                    words = story(words)
                    player.words = words
                    found = True
                    break

            # if player name is not in db, it creates new player object
            if found == False:
                words = story(words)
                player = Player(name, words)

            # adds player to list of players in current game
            current_players[name] = player

        # Print the name of player and their answers
        for player in current_players:
            print("\nHere is", str(current_players[player].name) + "'s story:")
            current_players[player].read_story()
            input("Press enter to continue.")

        # Each player votes
        for voter in current_players:
            i = 1
            for votee in current_players:
                print(f"\n{i}. {current_players[votee].name}")
                i += 1
            vote = validate_vote(
                current_players[voter].name, current_players)

            current_players[vote].vote += 1

        # Votes are compared and winner is announced
        votes = []
        for player in current_players:
            votes.append(current_players[player])
        winner = votes[0]

        for player in votes:
            if player.vote > winner.vote:
                winner = player

        winner.score += 1

        print('\nYour winner is', winner.name, 'with', winner.vote, 'votes!')

        # Resets players votes and words before adding to db
        for player in current_players:
            current_players[player].reset()

        # Adds the players in current game to to database
        add_to_database(current_players)

        # Continue game loop
        input("\nPress enter to go back to main menu. ")

    elif choice == '2' or choice == 'leaderboards':
        show_leaderboards()

    elif choice == '3' or choice == 'exit':
        print("\nSee you later!")
        break

    else:
        print("\nInvalid input")
