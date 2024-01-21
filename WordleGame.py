import os
import re

current_directory = os.getcwd()
allwords = open("Wordlists/words.txt", "r")
commonwords = open("Wordlists/commonwords.txt", "r")
commonwords_to_list = commonwords.read().split("\n")
words_to_list = allwords.read().split("\n")


class Wordle:
    list_of_words = []
    list_of_commonwords = []

    for words in words_to_list:
        list_of_words.append(words)

    for words in commonwords_to_list:
        list_of_commonwords.append(words)



    #RESULTS
    ATTEMPTS = 0



    def __init__(self, mode, answer, wordleStrategy):
        self.mode = mode
        self.answer = answer
        self.strategy = wordleStrategy

    def inputResult(self):
        while True:

            result = input('Result? ')
            if self.valid_result(result):
                return result
            else:
                print("Invalid result")

    def valid_result(self, result):
        if len(result) != 5:
            return False
        if not bool(re.match('^[012]+$', result)):
            return False
        return True

    def get_input_from_words(self, guess, correct_word):
        input = list('-----')
        answer = list(correct_word)
        index = 0
        for letter in guess:
            if letter == answer[index]:
                input[index] = '2'
                answer[index] = '-'
            else:
                if letter in answer:
                    input[index] = '1'
                else:
                    input[index] = '0'
            index += 1
        return ''.join(input)

    def reset_lists(self):
        self.list_of_words.clear()
        self.list_of_commonwords.clear()
        self.list_of_words.extend(words_to_list)
        self.list_of_commonwords.extend(commonwords_to_list)

    def benchmark(self):

        input = '-----'
        guess = ''
        while input != '22222':
            self.ATTEMPTS += 1

            guess = self.strategy.get_word(input, guess, self.list_of_words, self.list_of_commonwords)


            # Get input answer from guess
            input = self.get_input_from_words(guess, self.answer)
            print(guess)
        self.reset_lists()



    def solve_wordle(self, first_guess):
        input = ''
        guess = first_guess
        while input != '22222':
            input = self.inputResult()
            guess = self.strategy.get_word(input, guess, words_to_list, commonwords_to_list)
            print("Guess with word:" + guess)
        self.reset_lists()






