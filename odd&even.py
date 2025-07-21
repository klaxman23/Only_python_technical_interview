#Write a python program to print the odd and even number?

# num = [i for i in range(1,101)]

# print(num)

# print("Even number!!")
# num = [i for i in range(1,101) if i%2==0]
# print(num)

# print("Odd number!!")
# num = [i for i in range(1,101) if i%2==1]
# print(num)

num = int(input("Enter a value:"))

if num%2==0:
    print("Even number")
else:
    print("Odd number")