#8. Create a program that checks if a given string is a palindrome.
word = str(input("Enter word for palindrome = ")).lower()
if word == word[::-1]:
    print (f"{word} is a palindrom ")
else:
    print (f"{word} is not a palindrome")
print("+++++++++++++++++++++++++++++++++")
