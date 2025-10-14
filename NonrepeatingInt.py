#Write a python program to find the first non-repeating elements in given list of integer
workList = [100,101,231,1001,101,100,123] #input list

for num in workList: #for loop to iterate the elements
    if workList.count(num) == 1 :#to check how many times the number exists in the list if it is 1 then break the loop
        print("First non-repeating elements in given list of integers is ", num)
        break
    else:
        print("The list do not have non-repeating numbers")

