import random
from validWords import valid 

CHOSEN = random.choice(valid)
CHANCES = 7

class Color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
class Guess:
    counter = 1
    def __init__(self,w_str:str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""

    def increment(self):
        Guess.counter += 1
    def isValid(self):
        return self.w_str in valid


    def applyGreens(self):
        for i,_ in enumerate(self.w_chars):
            actualChar = CHOSEN[i]
            guessedChar = self.w_chars[i]
            if actualChar == guessedChar:
                colored =  f"{Color.GREEN}{actualChar}{Color.BASE}"
                self.w_chars[i] = colored
    
    def applyGuess(self):
        self.applyGreens()
        self.post_guess_w_str="".join(self.w_chars)
        print(self.post_guess_w_str)

