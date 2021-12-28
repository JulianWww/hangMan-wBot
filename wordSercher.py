from nltk.corpus import words
from random import choice
words = list(set([x.lower() for x in words.words()]))

class Search:
    def __init__(self, size):
        self.remaining = []
        self.checkedLetters = []
        for word in words:
            if len(word) == size:
                self.remaining.append(word)

    @staticmethod
    def isPossibleWord(word, known, tryed):
        for wchar, kchar in zip(list(word), list(known)):
            if kchar != "_":
                if wchar != kchar:
                    return False
            else:
                if wchar in tryed:
                    return False
        return True

    @staticmethod
    def doseNotContainAny(word, letters):
        for letter in letters:
            if letter in word:
                return False
        return True

    def getLetterCount(self):
        letters = {}
        for word in self.remaining:
            for letter in set(word):
                if not letter in self.checkedLetters:
                    try:
                        letters[letter] += 1
                    except:
                        letters[letter] = 1
        return letters

    def getNextLetter(self, tryed):
        count = self.getLetterCount()
        topLetters = []
        topOccourance = 0
        for letter, occourance in count.items():
            if not letter in tryed:
                if occourance > topOccourance:
                    topOccourance = occourance
                    topLetters = [letter]
                elif occourance == topOccourance:
                    topLetters.append(letter)

        return choice(topLetters)

    def refineSearch(self, known, tryed, wrong):
        self.checkedLetters = list(known.replace("_", ""))
        remaining = []
        for word in self.remaining:
            if self.isPossibleWord(word, known, tryed) and self.doseNotContainAny(word, wrong):
                remaining.append(word)
        self.remaining = remaining

    def getAction(self, known, tryed, wrong):
        self.refineSearch(known, tryed, wrong)
        return self.getNextLetter(tryed)

        
