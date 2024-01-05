"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):

        word_path = open(path)

        self.words = self.parse(word_path)

        print(f"{len(self.words)} words read")

    def parse(self, word_path):
        return [w.strip() for w in word_path]
    
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    
    def parse(self, word_path):

        return [w.strip() for w in word_path
                if w.strip() and not w.startswith("#")]

    