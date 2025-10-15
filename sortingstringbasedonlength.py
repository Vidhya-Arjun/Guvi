inputString = "Python is an amazing programming language"
splitString = inputString.split() #split string with delimiter space into list

for i in range(0,len(splitString)): # looping through the list
    for j in range(i,len(splitString)):#looping through to check least length of each element in list
        if (len(splitString[i]) > len(splitString[j])):
            splitString[i], splitString[j] = splitString[j], splitString[i] #swapping if least element is found
result = " ".join(splitString) #rephrasing into string
print(result)