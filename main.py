import os
import time

from WordleGame import Wordle
from Strategies import HModeSimple
from Strategies import NModeMaximizeEntropy
from Strategies import NModeMaximizeEntropyCommon
from Strategies import HModeMaximizeEntropyCommon
from Strategies import HModeMaximizeEntropy
from Strategies import HModeSimpleCommon
import sys




    # or other long operations

current_directory = os.getcwd()
wordleanswers = open("Wordlists/wordle_answers", "r")
words_to_list = wordleanswers.read().split("\n")
wordleanswers.close()


if __name__ == "__main__":
    """
    algorithm = NModeMaximizeEntropyCommon
    game = Wordle("spent", algorithm, "HARD")
    print("Guess with word: salet")
    game.solve_wordle('salet')
    """

    Total_Attempts = 0
    Words_Solved = 0
    Words_Not_Solved = 0
    List_Words_Not_Solved = []

    for word in words_to_list:
        sys.stdout.write("\rCompleted: %d/%d" % (Words_Solved, len(words_to_list)))
        algorithm = NModeMaximizeEntropy
        game = Wordle(word, algorithm, 'NORMAL')
        game.benchmark()

        Total_Attempts += game.ATTEMPTS

        if game.ATTEMPTS > 6:
            Words_Not_Solved += 1
            List_Words_Not_Solved.append(word)
        else:
            Words_Solved += 1
        bar = ''
        bar += "\u2588"

        sys.stdout.flush()

    Average_attempt = Total_Attempts / len(words_to_list)
    print("\nAverage: " + str(Average_attempt))
    print("Solved: " + str(Words_Solved))
    print("Words solved above 6 tries: " + str(Words_Not_Solved))
    print(List_Words_Not_Solved)

    """

    algorithm = NModeMaximizeEntropyCommon
    game = Wordle('splat', algorithm, 'NORMAL')
    game.benchmark()
    """