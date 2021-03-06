"""This module holds the class for each player"""

from game_pkg.stories import story


class Player:
    def __init__(self, name, words):
        self.name = name
        self.words = words
        self.score = 0
        self.vote = 0

    def read_story(self):
        print(story(self.words))

    def reset(self):
        self.words = {}
        self.vote = 0
