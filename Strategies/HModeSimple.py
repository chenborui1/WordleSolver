import random
import FilterPossibleWords

# Code base

def get_word(answer_input, word, common_words_list, all_words_list):

    optimizedList = FilterPossibleWords.analyze_result(word, answer_input, all_words_list)
    startWord = random.choice(optimizedList)

    return startWord

"""
*****RESULT*****
Completed: 2104/2315
Average: 4.719222462203024
Solved: 2104
Words solved above 6 tries: 211
['agent', 'agile', 'algae', 'amble', 'aping', 'aware', 'bacon', 'badge', 'baggy', 'basis', 'belly', 'berry', 'biddy', 'bitty', 'bongo', 'bonus', 'booby', 'booty', 'booze', 'boxer', 'brass', 'bread', 'buddy', 'bully', 'bushy', 'butch', 'buyer', 'cagey', 'canon', 'carry', 'carve', 'catch', 'cheer', 'chore', 'class', 'cleft', 'clone', 'coral', 'corer', 'coven', 'cover', 'cower', 'crack', 'crane', 'crass', 'crate', 'crave', 'creed', 'creek', 'cress', 'curve', 'daddy', 'dairy', 'dandy', 'defer', 'ditch', 'diver', 'dolly', 'dowel', 'draft', 'drake', 'dried', 'drill', 'drown', 'fanny', 'fatal', 'fault', 'fight', 'filly', 'finer', 'fixer', 'flame', 'flank', 'focus', 'found', 'freer', 'fried', 'froth', 'froze', 'fully', 'funny', 'gauge', 'gayer', 'girth', 'given', 'glare', 'glass', 'golly', 'goner', 'goofy', 'goose', 'grace', 'grape', 'grate', 'grave', 'gripe', 'handy', 'happy', 'hardy', 'hatch', 'hater', 'hilly', 'hippy', 'hobby', 'hutch', 'jelly', 'joist', 'jolly', 'jumpy', 'krill', 'lager', 'layer', 'lower', 'loyal', 'mamma', 'manly', 'might', 'moose', 'mover', 'munch', 'nerve', 'night', 'notch', 'otter', 'paint', 'pasta', 'paste', 'patch', 'pedal', 'penny', 'piggy', 'pitch', 'pixie', 'pizza', 'plead', 'polka', 'poppy', 'power', 'probe', 'prone', 'prose', 'prove', 'prude', 'puppy', 'rabid', 'rainy', 'rarer', 'rebel', 'relic', 'renew', 'rider', 'river', 'roger', 'rower', 'safer', 'sappy', 'savvy', 'scale', 'scion', 'scram', 'scrap', 'serum', 'sever', 'shank', 'shore', 'slime', 'smart', 'snake', 'sneer', 'spark', 'spasm', 'stake', 'steep', 'steer', 'stoke', 'stony', 'store', 'storm', 'study', 'sweep', 'swell', 'tabby', 'tacky', 'tamer', 'taper', 'taste', 'tight', 'trait', 'tripe', 'urine', 'valor', 'vaunt', 'verve', 'villa', 'viper', 'vogue', 'vouch', 'wacky', 'wafer', 'watch', 'waxen', 'weave', 'where', 'wight', 'winch', 'woken', 'woody', 'wooer', 'wooly', 'woozy', 'zonal']


"""
