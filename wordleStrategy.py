import os
import random

current_directory = os.getcwd()



file=open("words.txt", "r")

words = file.read()

words_to_list = words.split("\n")

file.close()

# print(words_to_list)



def find_first_guess(wordList):
    emptyList = []
    for word in wordList:
        counter = 0
        letters = set(word)
        for x in 'aeiou':
            if x in letters:
                counter += 1
        if counter == 4:
            emptyList.append(word)
            
    return emptyList


listOfMostUniqueVowels = find_first_guess(words_to_list)
random_most_unique_vowel_word = random.choice(listOfMostUniqueVowels)

print(random_most_unique_vowel_word)
    









