# Mathematical logic approach

def palindrome_checker(number):
    x = number
    rev = 0
    while x:
        rmn = x % 10
        rev = rmn + rev * 10
        x = x//10 # use // for integer divison

    if rev == number:
        print(f"Number {number} is palindrome number")
    else:
        print(f"Number {number} is not palindrome number")

palindrome_checker(121)
palindrome_checker(125)
