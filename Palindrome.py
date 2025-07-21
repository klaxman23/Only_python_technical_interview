# Write a python program for palondrome.

name = input("Enter a name:")
rev = name[::-1]
if name==rev:
    print("It is a palindrome!")
else:
    print("It is not a palinrome!")