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
    emptyList = []
    for everyword in wordList:

        if letter not in everyword:
            emptyList.append(everyword)
    return emptyList


def filter_words_with_letter(wordList, letter):
    emptyList = []
    for everyword in wordList:
        if letter in everyword:
            emptyList.append(everyword)
    return emptyList

def filter_words_wrong_position(wordList, index, letter):
    emptyList = []
    for everyword in wordList:
        if letter != everyword[index]:
            emptyList.append(everyword)
    return emptyList

def filter_words_correct_position(wordList, index, letter):
    emptyList = []
    for everyword in wordList:
        if letter == everyword[index]:
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


def analyze_result(wordUsed, userInput, wordList):
    index = 0
    print(wordList)

    for element in userInput:
        emptylist = []
        if element == '0':
            for i in range(5):
                if i != index:

            newlist = filter_words_no_letter(wordList, wordUsed[index])
            for newword in newlist:
                emptylist.append(newword)
        if element == '1':
            newlist = filter_words_with_letter(wordList, wordUsed[index])
            for newword in newlist:
                emptylist.append(newword)

            newsecondlist = filter_words_wrong_position(emptylist, index, wordUsed[index])
            emptylist.clear()
            for posiword in newsecondlist:
                emptylist.append(posiword)

        if element == '2':
            newlist = filter_words_correct_position(wordList,index, wordUsed[index])
            for newword in newlist:
                emptylist.append(newword)

        wordList.clear()
        for everyword in emptylist:
            wordList.append(everyword)

        index += 1
    return wordList


# Code base

listOfMostUniqueVowels = find_first_guess(words_to_list)
random_most_unique_vowel_word = random.choice(listOfMostUniqueVowels)

print("Suggested starting word: " + random_most_unique_vowel_word)

startWord = input("Chosen word: ")

while len(words_to_list) != 1:
    userInput = inputResult()
    print(userInput)
    optimizedList = analyze_result(startWord, userInput, words_to_list)

    startWord = random.choice(optimizedList)
    print("Guess with word: " + startWord)
