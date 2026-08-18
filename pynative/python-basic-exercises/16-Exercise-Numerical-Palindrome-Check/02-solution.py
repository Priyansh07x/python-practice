# Approach by converting the number into string and checking original str and reversed str
def palindrome_checker(num):
    original_str = str(num)
    reversed_str = original_str[::-1]

    if original_str == reversed_str:
        print(f"Number {num} is palindrome number")
    else:
        print(f"Number {num} is not palindrome number")

palindrome_checker(121)
palindrome_checker(125)
