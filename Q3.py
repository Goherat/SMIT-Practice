#3. Write a program that checks if a given year is a leap year.

year = int(input("Enter Year : "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
    print (f"{year} is leap year")
else:
    print (f"{year} is not a leap year")
print("++++++++++++++++++++++++++++++++++++++++++++++++")