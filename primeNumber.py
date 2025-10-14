#To find a prime number from a list and store it in another list

def primelist(numbers):
    primeList = [] #To intialise the primeList
    for num in numbers:
        if num > 1:
            for i in range(2,num//2):# when a number is prime when it is divided by itself or divided by 1
                if(num%i==0):
                    break # loops iterate to next number
            else:
                primeList.append(num)#if the condition not satisfied then the number is prime
    return primeList
primeList = primelist(originalList)
print(f"prime number list is {primeList}")
