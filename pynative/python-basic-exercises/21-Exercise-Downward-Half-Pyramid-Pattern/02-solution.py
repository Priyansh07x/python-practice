# Using reverse Iteration
# i = no. of stars
# So
# i decreases, stars decreases
for i in range(5,0,-1): # starts at 5, ends at 0, reduces by 1
    for j in range(i): # range(n) -> goes from 0 upto n-1
        print("*", end=" ")
    print()
