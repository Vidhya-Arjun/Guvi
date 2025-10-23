# write a list comprehension that creates a new list of squares of even numbers from a given list ,
# using a lambda function to check for even numbers
wishList = [1,2,4,56,7,8,98,99,90,5,100] #original list
evenList = list(filter(lambda x:x%2==0,wishList)) #condition to check even numbers using lambda
squareList = list(map(lambda y:y**2,evenList)) #iteration on squaring the even list
print(f"The evenlist {evenList} is \n" f"The squarelist{squareList}")
