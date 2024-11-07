# 14. Check if a year input by the user is a century year.

year = int(input("enter year = "))
if year % 100 == 0:
    print (f"{year} is century year")
else:
    print (f"{year} not a is century year")
