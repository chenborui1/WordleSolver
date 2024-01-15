import os
from WordleGame import Wordle
import wordleStrategy

current_directory = os.getcwd()
wordleanswers = open("Wordlists/wordle_answers", "r")
words = wordleanswers.read()
words_to_list = words.split("\n")
wordleanswers.close()

if __name__ == "__main__":



    for word in words_to_list:
        algorithm = wordleStrategy
        game = Wordle('HARD', word, algorithm)
        print(word)
        game.play()
        print(game.ATTEMPTS)


