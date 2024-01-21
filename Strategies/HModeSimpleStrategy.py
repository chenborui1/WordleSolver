import random
import FilterPossibleWords

# Code base

def get_word(answer_input, word, possible_guesses_list, common_words_list):
    if answer_input == '-----':
        return 'salet'
    else:
        startWord = word
    optimizedList = FilterPossibleWords.analyze_result(startWord, answer_input, possible_guesses_list)
    commonlist = FilterPossibleWords.list_with_common_words(optimizedList, common_words_list)
    if commonlist:
        startWord = random.choice(commonlist)

    else:
        startWord = random.choice(optimizedList)

    return startWord



