"""This module holds the menu and leaderboard screen"""


def main_menu():
    print()
    print("          === Madlibs Showdown ===          ")
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
