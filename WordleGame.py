
class Wordle:

    #RESULTS
    ATTEMPTS = 0



    def __init__(self, mode, answer, wordleStrategy):
        self.mode = mode
        self.answer = answer
        self.strategy = wordleStrategy


    def get_input_from_words(self, guess):
        input = list('-----')
        index = 0
        for letter in guess:
            if letter == self.answer[index]:
                input[index] = '2'
            else:
                if letter in self.answer:
                    input[index] = '1'
                else:
                    input[index] = '0'
            index += 1
        return ''.join(input)


    def play(self):
        input = '-----'
        guess = ''
        while input != '22222':
            self.ATTEMPTS += 1
            guess = self.strategy.get_word(input, guess)

            print(guess)
            # Get input answer from guess

            input = self.get_input_from_words(guess)

            print(input)





