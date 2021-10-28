"""This is the module that handles validation for names and voting"""


def validate_name(x):

    name = input(f"\nHello Player {x + 1}! What is your name? ")

    if len(name) < 2 or len(name) > 10:
        print("\nEnter a name between 2 and 10 characters")
        return validate_name(x)

    return name


def validate_vote(name, current_players):
    vote = input(
        f"\nHi {name}. Enter the name of the person you want to vote for: ")

    if vote not in current_players:
        print("\nName that you entered is not in the game. ")
        return validate_vote(name, current_players)

    return vote
