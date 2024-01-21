import os
from WordleGame import Wordle
from Strategies import HModeSimpleStrategy
from Strategies import NModeMaximizeEntropy
import sys




    # or other long operations

current_directory = os.getcwd()
wordleanswers = open("Wordlists/wordle_answers", "r")
words = wordleanswers.read()
words_to_list = words.split("\n")
wordleanswers.close()

if __name__ == "__main__":
    """
    Total_Attempts = 0
    Words_Solved = 0
    Words_Not_Solved = 0
    List_Words_Not_Solved = []

    for word in words_to_list:
        algorithm = HModeSimpleStrategy
        game = Wordle('HARD', word, algorithm)
        game.benchmark()
        Total_Attempts += game.ATTEMPTS
        if game.ATTEMPTS > 6:
            Words_Not_Solved += 1
            List_Words_Not_Solved.append(word)
        else:
            Words_Solved += 1
        bar = ''
        bar += "\u2588"
        sys.stdout.write("\rCompleted: %d/%d" % (Words_Solved, len(words_to_list)))
        sys.stdout.flush()





    Average_attempt = Total_Attempts / len(words_to_list)
    print("\nAverage: " + str(Average_attempt))
    print("Solved: " + str(Words_Solved))
    print("Failed: " + str(Words_Not_Solved))
    print(List_Words_Not_Solved)
    """
    """
    algorithm = HModeSimpleStrategy
    game = Wordle('HARD', "parer", algorithm)
    game.solve_wordle('salet')
        """


    algorithm = NModeMaximizeEntropy
    game = Wordle('HARD', 'parer', algorithm)
    game.benchmark()
    print(game.ATTEMPTS)

