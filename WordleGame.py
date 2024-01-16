import re


class Wordle:

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


    def benchmark(self):
        input = '-----'
        guess = ''
        while input != '22222':
            self.ATTEMPTS += 1
            guess = self.strategy.get_word(input, guess)


            # Get input answer from guess
            input = self.get_input_from_words(guess, self.answer)



    def play(self, first_guess):
        input = ''
        guess = first_guess
        while input != '22222':
            input = self.inputResult()
            guess = self.strategy.get_word(input, guess)
            print("Guess with word:" + guess)





