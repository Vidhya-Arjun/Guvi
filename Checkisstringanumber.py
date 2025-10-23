Stringnumber = "1234567890" # input
checkIsNumber = map(lambda x:x.isdigit(), Stringnumber)#map is used to navigate through elements in string and is digit check whether the element is digit
if all(checkIsNumber): #condition to display if it is a number or not
    print(f"The string {Stringnumber} is a number")
else:
    print(f"The string {Stringnumber} is not a number")


