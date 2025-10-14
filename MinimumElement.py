#find the minimum element in rated and sorted list
from numpy.ma.core import minimum

mylist = [123,34,0,24,-1,100]
#sorting mylist element first
for num in range(len(mylist)):
    for item in range(num+1,len(mylist)):
        if mylist[num] > mylist[item]:
            mylist[num], mylist[item] = mylist[item], mylist[num]
minimumelement = mylist[0]
print("the minimum value in the sorted list is" ,minimumelement)
