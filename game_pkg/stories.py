"""This Module holds all the possible stories and queries to collect those stories"""
import random


def story_one(words):
    if words == {}:
        body_part = input("Name a body part. \n")
        adjective = input("Name an adjective. \n")
        place = input("Name a city. \n")
        adjective2 = input("Name another adjective. \n")
        place2 = input("Name a state. \n")
        female_celebrity = input("Name a female celebrity \n")
        body_part3 = input("Name another body part. \n")
        male_celebrity = input("Name a male celebrity. \n")
        body_part2 = input("Name another body part. \n")
        adjective3 = input("Name another adjective. \n")
        body_part4 = input("Name another body part. \n")
        organ = input("Name an organ. \n")

        words.update(adjective=adjective, adjective2=adjective2, adjective3=adjective3, place=place, place2=place2, female_celebrity=female_celebrity,
                     male_celebrity=male_celebrity, body_part=body_part, body_part2=body_part2, body_part3=body_part3, body_part4=body_part4, organ=organ)

        return words

    else:

        return (f"\nOnce upon a time, at a place called {words['place']}, there was " +
                f"a {words['adjective']} princess named {words['female_celebrity']}.\nHer kingdom " +
                f"was huge, but her {words['body_part']} was bigger.\nShe was beautiful " +
                f"from her {words['body_part2']} to her {words['organ']}.\nOne day she saw a {words['adjective2']} " +
                f"prince named {words['male_celebrity']}.\nHe had a {words['adjective3']} face. As soon as " +
                f"his {words['body_part3']} touched her {words['body_part4']} they fell in love.\nThey " +
                f"got married in {words['place2']} the following day.\n")


def story_two(words):
    if words == {}:
        adjective = input("Name an adjective. \n")
        plural_noun = input("Name a plural noun. \n")
        ing_verb = input("Name a verb ending in -ing. \n")
        plural_noun2 = input("Name a plural noun. \n")
        female_celebrity_name = input("Name a female celebrity. \n")
        person = input("Name a person in the game. \n")
        silly_word = input("Name a silly word. \n")
        verb = input("Name a verb. \n")
        food = input("Name a the plural word of a food. \n")
        noun = input("Name a noun. \n")
        adjective2 = input("Name an adjective. \n")
        adjective3 = input("Name an adjective. \n")
        shoe = input("Name a type of shoe. \n")
        something_alive = input("Name something alive. \n")
        noun2 = input("Name a noun. \n")
        ing_verb2 = input("Name a verb ending in -ing. \n")
        noun3 = input("Name a noun. \n")
        silly_word2 = input("Name a silly word. \n")

        words.update(adjective=adjective, plural_noun=plural_noun, ing_verb=ing_verb, plural_noun2=plural_noun2, female_celebrity_name=female_celebrity_name, person=person, silly_word=silly_word, verb=verb,
                     food=food, noun=noun, adjective2=adjective2, adjective3=adjective3, shoe=shoe, something_alive=something_alive, noun2=noun2, ing_verb2=ing_verb2, noun3=noun3, silly_word2=silly_word2)
        return words

    else:

        return (f"\nOne of the most {words['adjective']} things about graduating is that my " +
                f"{words['plural_noun']} are {words['ing_verb']} a huge party.\nI decided to have a backyard " +
                f"barbeque for all of my family and {words['plural_noun2']}.\nI've invited my best friends {words['female_celebrity_name']}, {words['person']}, " +
                f"and of course my teacher, Ms. {words['silly_word']}.\nMy dad is going to {words['verb']} hamburgers and {words['food']} on his shiny new {words['noun']}.\n" +
                f"He always thinks his {words['food']} tastes really {words['adjective2']}, but I think they taste like {words['adjective3']} {words['shoe']}.\n" +
                f"My mom is going to make her famous {words['something_alive']} salad, which is my favorite {words['noun2']}.\nMom said after we finish {words['ing_verb2']}, " +
                f"we can go swimming in our new {words['noun3']} {words['silly_word2']}.\n")


# Selects random stories to play for each game
story = random.choice([story_one, story_two])
