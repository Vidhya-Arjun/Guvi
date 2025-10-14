#function to find first and last digit of the given sequence of number
def sum_of_first_and_last(number):
    string_value = str(number) #as string only can be used to iterate through sequence, hence the conversion

    first = int(string_value[0])  # first digit
    last = int(string_value[-1])  # last digit

    print("First digit:", first)
    print("Last digit:", last)

    total = first + last
    return total