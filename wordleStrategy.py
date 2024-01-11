import os
import random
import re

# Initialize word list
current_directory = os.getcwd()
file = open("words.txt", "r")
words = file.read()
words_to_list = words.split("\n")
print(len(words_to_list))
file.close()


# Methods

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


def filter_words_no_letter(wordList, letter):
    print(len(wordList))
    emptyList = []
    for everyword in wordList:

        if letter not in everyword:
            emptyList.append(everyword)
    print(emptyList)
    print(len((emptyList)))
    return emptyList

def filter_words_with_letter(wordList, letter):
    emptyList = []
    for everyword in wordList:
        if letter in everyword:
            emptyList.append(everyword)
    return emptyList


def valid_result(result):
    if len(result) != 5:
        return False
    if not bool(re.match('^[012]+$', result)):
        return False
    return True


def inputResult():
    while True:

        result = input('Result? ')
        if valid_result(result):
            return result
        else:
            print("Invalid result")


def analyze_result(wordUsed, userInput, availableAlphabets, wordList):
    index = 0
    for element in userInput:

        emptylist = []
        if element == '0':
            availableAlphabets = availableAlphabets.replace(wordUsed[index], '')
            print(availableAlphabets)
            newlist = filter_words_no_letter(wordList, wordUsed[index])
            for newword in newlist:
                emptylist.append(newword)
        if element == '1':
            pass
        if element == '2':
            pass
        wordList.clear()
        for refinedWords in emptylist:
            wordList.append(refinedWords)
        index += 1
    return wordList


# Code base

listOfMostUniqueVowels = find_first_guess(words_to_list)
random_most_unique_vowel_word = random.choice(listOfMostUniqueVowels)

alphabetsToUse = 'abcdefghijklmnopqrstuvwxyz'
suggestStartingWord = random_most_unique_vowel_word

print("Suggested starting word: " + suggestStartingWord)

startWord = input("Chosen word: ")

while len(words_to_list) != 1:
    userInput = inputResult()
    optimizedList = analyze_result(startWord, userInput, alphabetsToUse, words_to_list)
    words_to_list.clear()
    for word in optimizedList:
        words_to_list.append(word)
    #print("Guess with word: " + random.choice(words_to_list))
