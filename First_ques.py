# Write a program in a string value only print the not duplicate values.
a = "Abbcdefghgh"

for i in a:
    if a.count(i)==1:
        print(i,end=",")
    
    