number = 7536
print(f"Given number: {number}")
rev = 0
while number > 0:
    rem = number % 10
    rev = rem + rev * 10
    number = number // 10

print(rev)

# If you need space between each digit
# while number > 0:
#     rem = number % 10

#     number = number // 10
#     print(rem, end=" ")
