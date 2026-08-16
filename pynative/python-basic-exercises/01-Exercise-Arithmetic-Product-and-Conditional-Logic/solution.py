a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

def product_or_sum(a, b):
    prod = a * b

    if prod <= 1000:
        return prod
    return a + b

result = product_or_sum(a,b)
print(f"The result is {result}.")
