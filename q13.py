row = 8
for i in range(1,row+1):
    print(" " * (row-i), end="  ")
    print("* " * i)



row1 = 8
for i in range(1 , (row1 + 1)):
    print(" " * (row1 - i), end= " ")
    print("+ " *i)


row2 = 9
for i in range(1, row2 + 1):
    print(" " * (row2 -i ),end=" ")
    print ("° " * i)