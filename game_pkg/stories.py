

def story_one(player_position):
    words = {}

    name = input(f"Hello Player {player_position + 1}! What is your name? ")
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

    return name, words
