num = int(input("Enter the number: "))

factorial = 1
# we started the loop from 1 because factorial is 1 for 0! and 1!
for i in range(1, num + 1):
    factorial *= i
print("The factorial of", num, "is", factorial)
