#you have been given a python list [10,20,30,9] and a value of 59. write a python program to find triplet in this list whose sum is equal to the given value
#_____________________________________________________________________________________________________________________________________________________
#logical understanding
#any three element sum leads to 59 or not that is the understanding and hence coded in this way
sampleList = [10,20,30,9] #defining input
target = 59 #target value
found = False #intialising flag

for i in range(len(sampleList)):#first iteration
    for j in range(i+1,len(sampleList)):#second iteration
        for k in range(j+1,len(sampleList)):#third iteration
            if sampleList[i] + sampleList[j] + sampleList[k] == target:#taget value
                found = True
                print("we have expected value from the triplet element of sample list")
                break #flag is set true and code stops 
        if found:
            break
    if found:
        break
    else:
        print("No triplets make the target value")