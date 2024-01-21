import os
import FilterPossibleWords
import math

current_directory = os.getcwd()
allwords = open("Wordlists/words.txt", "r")
possible_comb = open("Wordlists/output.txt", "r")
words_to_list = allwords.read().split("\n")
comb_to_list = possible_comb.read().split("\n")


def get_input_from_words(guess, correct_word):
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


def get_word(answer_input, word, possible_answers_list, common_words_list):
    if answer_input == '-----':
        return 'salet'
    else:
        startWord = word

    optimizedList = FilterPossibleWords.analyze_result(startWord, answer_input, possible_answers_list)

    if len(optimizedList) == 1:
        return optimizedList[0]
    empty_list = []
    empty_list.extend(optimizedList)
    commonlist = FilterPossibleWords.list_with_common_words(optimizedList, common_words_list)
    highest_entropy_words = []

    entropy = 0

    for word in words_to_list:

        information = get_expected_max_entropy(word, optimizedList)
        optimizedList.clear()
        optimizedList.extend(empty_list)

        if information > entropy:

            entropy = information
            highest_entropy_words.append(word)

    if(len(highest_entropy_words) == 0):
        return optimizedList[0]

    return highest_entropy_words[-1]

def get_expected_max_entropy(word, optimized_list):
    previous_size = len(optimized_list)
    empty_list = []
    empty_list.extend(optimized_list)
    added_bits = 0
    collect_input = []
    for input in comb_to_list:
        collect_input.append(input)
        new_list_size = len(FilterPossibleWords.analyze_result(word, input, optimized_list))
        probability = new_list_size/previous_size
        if probability != 0:
            added_bits += math.log(1/probability, 2)
    expected_information = added_bits/len(empty_list)


    return expected_information

