import os

path = "C:\\Users\\chenb\\Desktop\\Projects\\WordleAlgorithm\\"
os.chdir(path)

file=open("words.txt", "r")

words = file.read()

words_to_list = words.split("\n")

file.close()



