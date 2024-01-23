
import FilterPossibleWords
import math




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


def get_word(answer_input, word, common_words_list, words_to_list):

    optimizedList = FilterPossibleWords.analyze_result(word, answer_input, words_to_list)



    if len(optimizedList) == 1:


        return optimizedList[0]
    empty_list = []
    empty_list.extend(optimizedList)

    highest_entropy_words = []

    entropy = 0

    for word in optimizedList:

        information = get_expected_max_entropy(word, optimizedList)
        optimizedList.clear()
        optimizedList.extend(empty_list)

        if information > entropy:

            entropy = information
            highest_entropy_words.append(word)


    return highest_entropy_words[-1]

def get_expected_max_entropy(word, optimized_list):

    previous_size = len(optimized_list)
    empty_list = []
    empty_list.extend(optimized_list)

    added_bits = 0


    for optimize_word in optimized_list:

        input = get_input_from_words(word, optimize_word)
        new_list_size = len(FilterPossibleWords.analyze_result(word, input, optimized_list))

        probability = new_list_size/previous_size
        optimized_list.clear()
        optimized_list.extend(empty_list)

        if probability != 0:

            added_bits += math.log(1/probability, 2)

    expected_information = added_bits/len(empty_list)

    return expected_information

"""
*****RESULT*****
Completed: 2225/2315
Average: 4.247516198704104
Solved: 2225
Words solved above 6 tries: 90
['ankle', 'aping', 'boozy', 'boxer', 'buggy', 'clove', 'corer', 'cover', 'crass', 'craze', 'diver', 'dutch', 'fewer', 'fixer', 'frank', 'gazer', 'grant', 'gully', 'hatch', 'hitch', 'hover', 'irate', 'jelly', 'joker', 'jolly', 'krill', 'ladle', 'layer', 'liner', 'maker', 'mammy', 'might', 'mound', 'mushy', 'musty', 'pasty', 'patch', 'patty', 'penny', 'pitch', 'pound', 'prank', 'prone', 'punch', 'purer', 'pushy', 'putty', 'rider', 'right', 'river', 'rover', 'rower', 'saner', 'sassy', 'savvy', 'sever', 'shame', 'slush', 'sneer', 'spool', 'staid', 'state', 'stave', 'steer', 'stoic', 'stout', 'stove', 'straw', 'stray', 'swell', 'taint', 'taper', 'taunt', 'tight', 'tripe', 'trite', 'vaunt', 'wager', 'watch', 'water', 'wider', 'wight', 'willy', 'witch', 'witty', 'woody', 'worse', 'wrack', 'wrest', 'zesty']


"""