# 17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
num = int(input("enter a number = "))
div_2 = 2
div_3 = 3
if num % 2 == 0 and num % 3 == 0:
    print ( f" {num} is divisible by {div_2} , {div_3} or both")
elif num % div_2 ==0:
    print ( f" {num} is divisible by {div_2} only ")
elif num % div_3 == 0:
    print ( f" {num} is divisible by {div_3} only ")
else:
    print ( f" {num} is not divisible by 2, 3, or both")
    