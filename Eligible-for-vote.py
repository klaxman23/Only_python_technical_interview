# Take the user request and find the user eligible for vote or not.

name = input("Enter a user name:")
age = int(input("Enter a age:"))
city = (input("Enter the born city name:"))
print("=======================")
print("User name:",name)
print("User age:",age)
print("User born city:",city)

if age>18:
    print("User eligible for vote.")
else:
    print("User not eligible for vote.")
    