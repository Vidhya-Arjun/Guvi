import random

#List of words used for scrambling
wordlist = ['python','javasscript','java','automation','pytest','guvi','selenium']

#Using random function one word is picked randomly
word = random.choice(wordlist)
print(word)
#assigning the string to a variable inorder to split into character
wordletter = list(word)
print(wordletter)
#Word shuffling takes place here
random.shuffle(wordletter)
#joining of jumbling words happen here
scrambled_word = ''.join(wordletter)
#sorting done for uniformity and comparasion
sortedwordlist = sorted(scrambled_word)
print(sortedwordlist)

print("Please enter any one of the word from the list wordlist ['python','javasscript','java','automation','pytest','guvi','selenium']")

loop = True # to make loop active
while loop:
    userguess = "" # reintiate to avoid the appending of old values
    UserInput = input("Enter a word: ")

#loop through the words from the input
    for i in UserInput:
            userguess += i

            if sorted(userguess) == sortedwordlist:
                print("Correct!")
                loop = False # on condition is satisfied the loop teriminated
            else:
                print("Incorrect!")
