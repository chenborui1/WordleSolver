import os
from WordleGame import Wordle
import WordleHardStrategy

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
        algorithm = WordleHardStrategy
        game = Wordle('HARD', word, algorithm)

        game.benchmark()
        Total_Attempts += game.ATTEMPTS
        if game.ATTEMPTS > 6:
            Words_Not_Solved += 1
            List_Words_Not_Solved.append(word)
        Words_Solved += 1
        print(Words_Solved)

    Average_attempt = Total_Attempts / len(words_to_list)
    print("Average: " + str(Average_attempt))
    print("Failed: " + str(Words_Not_Solved))
    print(List_Words_Not_Solved)
    """
    algorithm = WordleHardStrategy
    game = Wordle('HARD', "",algorithm)
    game.play('salet')