numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# FUnction to return the boolean flag
# def use_list(my_list):
#     left = 0
#     right = -1
#     if my_list[left] == my_list[right]:
#         return True
#     else:
#         return False

# Concise way
def use_list(my_list):
    return my_list[0] == my_list[-1]

print(f"Given list: {numbers_y} | result is {use_list(numbers_y)}")
print(f"Given list: {numbers_x} | result is {use_list(numbers_x)}")

# FUnction to print the complete result
# def use_list(my_list):
#     if my_list[0] == my_list[-1]:
#         print(f"Given list: {my_list} | result is True")
#     else:
#         print(f"Given list: {my_list} | result is False")
