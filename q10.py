# 9. Write a program to print the first 10 Fibonacci numbers.
# 0+1=1
# 1+1=2
# 2+1=3
# 3+2=5
# 5+3=8
# 8+5=13


fibNum = 0
i = 1
while i < 100:
    fibNum += i
    i = i + fibNum
    print("fin number = ", fibNum)





fibLenght = 10
fib1 = 0
fib2 = 1
i = 0
while i < fibLenght:
    fibnumber = fib1 + fib2
    fib1 = fib2
    fib2 = fibnumber
    i += 1
    print ( f" fibNumner @ {i} = {fibnumber} ")