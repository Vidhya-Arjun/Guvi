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
