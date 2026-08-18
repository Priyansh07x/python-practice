def my_func(lst1, lst2):
    res1 = []
    res2 = []
    # odd numbers from the 1st list
    for x in lst1:
        if x % 2 != 0:
            res1.append(x)

    for y in lst2:
        if y % 2 == 0:
            res2.append(y)

    return res1 + res2

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(my_func(list1, list2))
