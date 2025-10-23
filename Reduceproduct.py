#Given a list of numbers, use the reduce function and a lambda expression
# to calculate the product of all the numbers in the list
from functools import reduce # reduce should be imported form functools library

samplelist = [5,2,4,3,6,7] #original list
productlistusingreduce = reduce(lambda x,y:x*y, samplelist)# product of listr
print(productlistusingreduce) #printing the product