rows = 5
# number of stars = rows - i + 1
# so
# i -> increases
# stars -> decrease
for i in range(1, rows + 1):
    for j in range(i, rows + 1):
        print("*", end=" ")

    print("\n")
