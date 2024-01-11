import os
import random
import re

#Initialize word list
current_directory = os.getcwd()
file=open("words.txt", "r")
words = file.read()
words_to_list = words.split("\n")
file.close()


#Methods

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

def validResult(result):
    checkerForInteger = False
    if len(result) != 5:
        return False
    if not bool(re.match('^[012]+$', result)):
        return False
    return True


def inputResult():
    while True:
    
        result = input('Result? ')
        if validResult(result):
            return result
        else:
            print("Invalid result")

def analyze_result(wordUsed, userInput, availableAlphabets):
    
    #Need to update word alphabets based on user input
    #Analyze user input and word used to change availableAlphabets
    #Ultimately get the next best word to try

    #First reduce word list length by getting rid of all alphabets that are not present
    index = 0
    for element in userInput:
        if element is '0':
            availableAlphabets = availableAlphabets.replace(wordUsed[index], '')
        if element is '1':
            availableAlphabets = availableAlphabets.replace(wordUsed[index], '')
        if element is '2':
            availableAlphabets = availableAlphabets.replace(wordUsed[index], '')
        index += 1
    print(availableAlphabets)
            


    


#Code base
    
listOfMostUniqueVowels = find_first_guess(words_to_list)
random_most_unique_vowel_word = random.choice(listOfMostUniqueVowels)

alphabetsToUse = 'abcdefghijklmnopqrstuvwxyz'
firstWord = random_most_unique_vowel_word

print("Put in: " + random_most_unique_vowel_word)

# Input 5 digit number that consists of only 0, 1, or 2
# Where 0 is that letter is not present
# Where 1 is that letter is present but not at the correct index
# Where 2 is that is at the correct spot

analyze_result(firstWord, inputResult(), alphabetsToUse)





    


    









