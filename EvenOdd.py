# To print even numbers and odd numbers from an original List
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