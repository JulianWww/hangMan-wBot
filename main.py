from json import load as json_load
from wordSercher import Search, words, choice

with open("data/lives.json", "r") as file:
    states = json_load(file)


class ConsoleAgent():
    def getAction(self, *args):
        g = input("guess: ")
        if len(g) != 1:
            print("one character only")
            return self.getAction(*args)
        if not g.islower():
            print("lower case letter only")
            return self.getAction(*args)
        return g

class SlowSerch(Search):
    def getAction(self, *args):
        letter = super(SlowSerch, self).getAction(*args)
        print(len(self.remaining), "words left")
        return letter

class Game:
    def __init__(self, word, player):
        if not word in words:
            raise ValueError(f"{word} is not a recognized word")

        print(word)
        self.word = word
        self.player = player
        self.known = "_"*len(word)
        self.guessed = set()
        self.wrong = set()
        self.life = 0
        self.done = False
        self.win = None

    def guess(self, letter):
        self.guessed.add(letter)
        if not letter in self.word:
            self.life += 1
            self.wrong.add(letter)

        else:
            k = list(self.known)
            for idx, l in enumerate(self.word):
                if letter == l:
                    k[idx] = l

            self.known = "".join(k)

    def render(self):
        print(states[self.life])
        print()
        print("word:", "".join([x + " " for x in self.known]))
        print("done:", "".join([x + " " for x in self.guessed]))

        letter = self.player.getAction(self.known, self.guessed, self.wrong)
        self.guess(letter)

        if (self.life == len(states)-1):
            print("you Loose")
            self.win = False
            self.done = True
            
        if ("_" not in self.known):
            print("you win")
            self.win = True
            self.done = True

word = input("plz enter a word: ")
if word == "":
    word = choice(words)
try:
    game = Game(word, SlowSerch(len(word)))
except ValueError:
    print(f"Im sory I only know {len(words)} words and '{word}' is not one of them.")
    d = input("would you like me to list all valid words? [Y/n]")
    if d.upper() == "Y":
        print("just remember you wanted this")
        print(words)
    else:
        print("choosing a random word")
        word = choice(words)
        game = Game(word, SlowSerch(len(word)))


    
while not game.done:
    game.render()

print("the word was",game.word)
