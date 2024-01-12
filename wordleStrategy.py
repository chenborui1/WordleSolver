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


def contains_duplicate_letter(word, index):
    for i in range(len(word)):
        if i != index and word[i] == word[index]:
            return True
    return False


def grey_all_duplicates(word, letter, index, userinput):
    for i in range(5):
        if word[i] == letter and userinput[i] != '0':
            return False
    return True

def prioritize_unique_letters(optimizedlist):
    emptylist = []
    for words in optimizedlist:
        if len(set(words)) == len(words):
            emptylist.append(words)

    return emptylist






def analyze_result(wordUsed, userInput, wordList):
    index = 0


    for element in userInput:
        emptylist = []
        if element == '0':
            if not contains_duplicate_letter(wordUsed, index):
                newlist = filter_words_no_letter(wordList, wordUsed[index])
                for newword in newlist:
                    emptylist.append(newword)
            else:
                if grey_all_duplicates(wordUsed, wordUsed[index], index, userInput):
                    newlist = filter_words_no_letter(wordList, wordUsed[index])
                    for newword in newlist:
                        emptylist.append(newword)
                else:
                    for newword in wordList:
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
    optimizedList = analyze_result(startWord, userInput, words_to_list)
    if not prioritize_unique_letters(optimizedList):
        startWord = random.choice(optimizedList)
    else:
        startWord = random.choice(prioritize_unique_letters(optimizedList))

    print("Guess with word: " + startWord)

