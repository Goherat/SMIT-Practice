# 19. Check if a string input is uppercase, lowercase, or a mix.
string = str(input("Enter a word = "))
if string.islower():
    print(f"{string} is in lower case")
elif string.isupper():
    print(f"{string} is in upper case")
else:
    print(f"{string} is in mix case")
    