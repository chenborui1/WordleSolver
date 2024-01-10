import os

current_directory = os.getcwd()



file=open("words.txt", "r")

words = file.read()

words_to_list = words.split("\n")

file.close()

print(words_to_list)



