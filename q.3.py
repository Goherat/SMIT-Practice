#  3. Write a program to calculate the sum of all numbers between 1 and 100.
for i in range(1,101,1):
    print (f"sum in for loop {i} + {i} = {i + i }")
j = 100 
while j < 200:
    j += 1
    print (f"sum in while loop {j} + {j} = {j + j }")
for q in range(i,j,1):
    print (f"q in for loop = {j*i } ")
    