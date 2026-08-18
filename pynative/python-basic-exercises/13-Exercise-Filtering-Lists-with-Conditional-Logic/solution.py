num_list = [10, 20, 33, 46, 55]
print("Given list is", num_list)
print("Divisible by 5:")
for i in num_list:
    if i % 5 == 0: # The modulo operator returns the remainder.
        print(i)
