import random


class WordMachine:

    def __init__(self):
        self.words = []
        self.served_words = []
        self.correct_words = []
        self.score = 0
        self.current_word = 0
        with open("words.txt") as file:
            self.words = file.readlines()
            self.words = [word.replace("\n", "") for word in self.words]
            self.get_random_words(200)

    def get_random_words(self, number):
        self.words = random.sample(self.words, number)

    def check_word(self, word):
        typed_word = word.lower().strip()
        if self.words[self.current_word] == typed_word:
            self.correct_words.append(self.words[self.current_word])
            self.calculate_score()
            return True
        return False

    def serve_another_word(self):
        self.served_words.append(self.words[self.current_word])
        self.current_word += 1

    def calculate_score(self):
        self.score = len(self.correct_words)

    def current_accuracy(self):
        return int(len(self.correct_words) / len(self.served_words) * 100)

    def restart(self):
        self.words = []
        self.served_words = []
        self.correct_words = []
        self.score = 0
        self.current_word = 0
        with open("words.txt") as file:
            self.words = file.readlines()
            self.words = [word.replace("\n", "") for word in self.words]
            self.get_random_words(200)

