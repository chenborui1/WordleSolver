import os
import random
import re

# Initialize word list

current_directory = os.getcwd()
allwords = open("Wordlists/words.txt", "r")
commonwords = open("Wordlists/commonwords.txt", "r")
words = allwords.read()
commonwords_to_list = commonwords.read().split("\n")
words_to_list = words.split("\n")


commonwords.close()
allwords.close()

# CONSTANTS
LETTERS_NOT_USED = 'abcdefghijklmnopqrstuvwxyz'

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

def list_with_common_words(optimizedlist):
    emptylist = []
    for word in optimizedlist:
        if word in commonwords_to_list:
            emptylist.append(word)
    return emptylist

def get_word_with_most_recurring_letter(optimizedlist, letters_not_used):

    emptylist = []
    letter_number = 0
    for letter in letters_not_used:
        list_of_words_with_letter = []
        for word in optimizedlist:
            if letter in word:
                list_of_words_with_letter.append(word)
        if len(list_of_words_with_letter) >= letter_number:
            letter_number = len(list_of_words_with_letter)
            emptylist.append(letter)
    most_letter = emptylist[-1]
    for word in optimizedlist:
        if most_letter in word:
            return word
        else:
            return random.choice(optimizedlist)





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
                    newlist = filter_words_wrong_position(wordList, index, wordUsed[index])
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

        global LETTERS_NOT_USED
        LETTERS_NOT_USED = LETTERS_NOT_USED.replace(wordUsed[index], '')
        index += 1
    return wordList


# Code base

def get_word(answer_input, word):
    if answer_input == '-----':
        global words_to_list
        words_to_list = words.split("\n")

        global LETTERS_NOT_USED
        LETTERS_NOT_USED = 'abcdefghijklmnopqrstuvwxyz'
        listOfMostUniqueVowels = find_first_guess(words_to_list)
        random_most_unique_vowel_word = random.choice(listOfMostUniqueVowels)
        return 'salet'
    else:
        startWord = word


    optimizedList = analyze_result(startWord, answer_input, words_to_list)
    commonlist = list_with_common_words(optimizedList)
    if commonlist:
        startWord = random.choice(commonlist)
    else:
        startWord = random.choice(optimizedList)
    print(len(optimizedList))
    return startWord



