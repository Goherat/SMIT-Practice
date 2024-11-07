# 20. Create a program that evaluates if an inputted number is prime.
num = int(input("Enter Number to check Prime Number = "))

sqrRoot = int(num ** 0.5)
for i in range(2, sqrRoot):
    if num % i == 0:
        print (num, "is a not prime number")
        
    else:
        print (f"{num} is a prime number")
    break