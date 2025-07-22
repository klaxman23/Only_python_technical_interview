#Write a program to print the sum of the n numbers.
num = int(input("Enter a value:"))
sum = 0
for i in range(num+1):
    sum = sum+i
print(f"{num} sum of n numbers{sum}")