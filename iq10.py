# 10. Use a loop to count the number of digits in an integer
num = int(input("enter your number = "))
str_num = str(num)
for i in str_num:
    print (f"{i} ")
    int_i = int(i)
    j = 0
    j += int_i
    print (f"{i} & {j}")
