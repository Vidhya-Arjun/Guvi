samplelist = [4, 2, -3, 1, 6]
found = False
for i in range(len(samplelist)):
    sumofsample = 0
    for j in range(i,len(samplelist)):
        sumofsample += samplelist[j]
        if sumofsample == 0:
            found = True
            break
if found:
    print("There exist sublist whose sum is 0")
else:
    print("There doesn't exist sublist whose sum is 0")


