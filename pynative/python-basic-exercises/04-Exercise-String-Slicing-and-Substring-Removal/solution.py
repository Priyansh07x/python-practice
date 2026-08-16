def remove_chars(s, n):
    return s[n:]

s = input("Enter a string: ")
n = int(input("Enter the number of characters to remove: "))
result = remove_chars(s, n)
print(result)
