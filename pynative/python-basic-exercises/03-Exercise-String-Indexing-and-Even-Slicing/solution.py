a = "pynative"
print("Original String is ", a)
print("Printing only even index chars")
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i])
