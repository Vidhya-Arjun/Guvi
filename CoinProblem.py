
def coin_prob(thisdict,target):
    total = 0

    for key,value in thisdict.items():
        updated_value = target//key
        thisdict[key] = updated_value
    return(thisdict)

thisdict = {10: 0, 5: 0 ,2:0,1: 0}
target = 10
print(coin_prob(thisdict,target))