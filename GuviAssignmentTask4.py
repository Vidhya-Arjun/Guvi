# To print even numbers and odd numbers from an original List
from babel import numbers
from scripts.regsetup import examples

originalList = [101,501,22,37,100,999,87,351]
def even_odd(numbers):
    even = [] #intialising even List to assign even values
    odd = [] #intialising odd List to assign odd values
    for item in numbers:
        if(item%2)==0:
            even.append(item)
        else:
         odd.append(item)
    return even,odd
evenList,oddList = even_odd(originalList)
print(f"even list values {evenList}")
print(f"odd list values {oddList}")
#______________________________________________________________________________________
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

#______________________________________________________________________________________
#To find a happy number from a list and store it in another list
# Happy numbers are the numbers whose indivual digits squares sum leads to 1
# if not the cycle of numbers will be repeated again
# 1 ^ 2 + 9 ^ 2 = 82
# 8 ^ 2 + 2 ^ 2 = 68
# 6 ^ 2 + 8 ^ 2 = 100
# 1 ^ 2 + 0 ^ 2 + 0 ^ 2 = 1
# As we reached to1, 19 is a Happy Number.
# Not a Happy number example, lets take example 20
# 2^2 + 0^2 = 4
# 4^2 = 16
# 1^2 + 6^2 = 37
# 3^2 + 7^2 = 58
# 5^2 + 8^2 = 89
# 8^2 + 9^2 = 145
# 1^2 + 4^2 + 5^2 = 42
# 4^2 + 2^2 = 20 --cycle repeating ,i.e 20 is repeating hence it is not a happy number

numbers = [101, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = []
def numSquareSum(n):
    squareSum = 0
    while (n != 0):
        squareSum += (n % 10) * (n % 10)
        n = n // 10
    return squareSum
def happyNumbers(numbers):
    happy_numbers =[]
    for num in numbers:
        seen = set()
        n = num
        while n != 1 and n not in seen:
            seen.add(n)
            n = numSquareSum(n)
            if n == 1:
                happy_numbers.append(num)
    return happy_numbers
happyNumberslist = happyNumbers(originalList)
print(f"happy numbers list is {happyNumberslist}")

# for num in numbers:
#     seen = set()
#     n = num
#     while n != 1 and n not in seen:
#         seen.add(n)
#         n = sum(int(digit) ** 2 for digit in str(n))
#     if n == 1:
#         happy_numbers.append(num)
#
# print("Happy numbers in the list:", happy_numbers)

# def happyNumbers(numbers):
#     happy_numbers = []
#     for num in numbers:
#         seen = set()
#         n = num
#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = sum(int(digit) ** 2 for digit in str(n))
#         if n == 1:
#             happy_numbers.append(num)
#     return happy_numbers
#
# happyNumberslist = happyNumbers(originalList)
# print(f"happy numbers list is {happyNumberslist}")
#-------------------------------------------------------------------------------------------------------------
#function to find first and last digit of the given sequence of number
def sum_of_first_and_last(number):
    string_value = str(number) #as string only can be used to iterate through sequence, hence the conversion

    first = int(string_value[0])  # first digit
    last = int(string_value[-1])  # last digit

    print("First digit:", first)
    print("Last digit:", last)

    total = first + last
    return total

