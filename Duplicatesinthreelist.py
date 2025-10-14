#to find duplicates of elements from 3 list
#finding duplicates which is common in all three list
Firstlist = [10,2,30,4,5,65,7,8,9]
Secondlist = [9,0,30,12,8,6,71,8,10]
thirdlist = [1,20,31,10,5,65,7,81,9]
resultList = [] # to store result

for item in Firstlist:
    if item in Secondlist and item in thirdlist and item not in resultList: #logic to check the duplicates in other two list
        resultList.append(item)

print(resultList)