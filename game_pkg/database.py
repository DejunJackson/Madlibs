
"""This module handles the MySQL database interactions by adding players to it and updating all player's scores during each game"""
import mysql.connector
from game_pkg.player import Player
import config

# Adds each new player to the database or updates old ones


def add_to_database(current_players):
    connection = mysql.connector.connect(
        host=config.host_name, user=config.user_name, passwd=config.db_passwd, database=config.database_name)

    cursor = connection.cursor(buffered=True)
    cursor.execute(
        """SELECT * from player""")
    records = cursor.fetchall()

    cursor.execute("SELECT PlayerName FROM Player")
    for player in current_players:
        found = False
        for row in records:
            if current_players[player].name == row[1]:
                cursor.execute(
                    "UPDATE player SET PlayerName = (%s), PlayerScore = (%s) WHERE PlayerName = (%s)", (current_players[player].name, current_players[player].score, current_players[player].name))
                found = True
                continue
        if found:
            continue
        else:
            cursor.execute(
                """INSERT INTO player (PlayerName, PlayerScore) VALUES (%s, %s)""", (current_players[player].name, current_players[player].score))

    connection.commit()
    cursor.close()


# adds new players from database to the all_players list in game to use for leaderboards, etc
def update_all_players(all_players):
    connection = mysql.connector.connect(
        host=config.host_name, user=config.user_name, passwd=config.db_passwd, database=config.database_name)

    cursor = connection.cursor(buffered=True)

    cursor.execute(
        """SELECT * from player""")
    records = cursor.fetchall()

    for row in records:
        player = Player(row[1], {})
        player.score = row[2]
        all_players.append(player)

    connection.commit()
    cursor.close()
    return all_players

# Queries database, orders by score in descending order and displays leaderboard


def show_leaderboards():
    connection = mysql.connector.connect(
        host=config.host_name, user=config.user_name, passwd=config.db_passwd, database=config.database_name)

    cursor = connection.cursor(buffered=True)

    cursor.execute(
        """SELECT PlayerName, PlayerScore from player ORDER BY PlayerScore DESC""")
    records = cursor.fetchall()
    if len(records) == 0:
        print('\nThere are no scores to print at this time. Go play some games!')
    elif len(records) == 1:
        print("------------------------------------------")
        print("|    Player                Score         |")
        print("------------------------------------------")
        print(
            f'\n     1.{records[0]}                    {records[1]}')
    else:
        position = 1
        print("------------------------------------------")
        print("|    Player                Score         |")
        print("------------------------------------------")
        for row in records:

            print(
                f'\n    {position}.{row[0]:<23} {row[1]}')

            position += 1

    connection.commit()
    cursor.close()
