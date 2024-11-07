# 9. Take three sides of a triangle as input and check if they form a valid triangle.
a = float(input("Enter Side a of triangle = "))
b = float(input("Enter Side b of triangle = "))
c = float(input("Enter Side c of triangle = "))
if a + b > c and b + c > a and c + a > b:
    print ("according to triangle theomram it's a Valid Triangle")
else:
    print ("according to triangle theomram it's not a Valid Triangle")
print("++++++++++++++++++++++++++++")
