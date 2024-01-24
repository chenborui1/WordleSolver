import random
import FilterPossibleWords

# Code base

def get_word(answer_input, word, common_words_list, all_words_list, answer_list):

    optimizedList = FilterPossibleWords.analyze_result(word, answer_input, all_words_list)
    commonlist = FilterPossibleWords.list_with_common_words(optimizedList, common_words_list)
    if commonlist:
        startWord = random.choice(commonlist)

    else:
        startWord = random.choice(optimizedList)
    return startWord

"""
*****RESULT*****
Completed: 2252/2315
Average: 4.042764578833693
Solved: 2252
Words solved above 6 tries: 63
['alike', 'axion', 'bawdy', 'bezel', 'biddy', 'binge', 'boxer', 'brake', 'broke', 'buddy', 'caper', 'chard', 'corer', 'cover', 'crane', 'defer', 'dilly', 'disco', 'dolly', 'dryer', 'erode', 'fight', 'foyer', 'freed', 'gaffe', 'gayer', 'geeky', 'giver', 'goner', 'graze', 'grill', 'hatch', 'hippy', 'hound', 'hover', 'jazzy', 'joker', 'kitty', 'melee', 'mound', 'nosey', 'ovate', 'pasta', 'pizza', 'power', 'prime', 'pushy', 'roger', 'rower', 'sassy', 'savor', 'shame', 'skier', 'stash', 'stoke', 'taunt', 'trope', 'wacky', 'waste', 'wheel', 'willy', 'witch', 'wreak']


"""
