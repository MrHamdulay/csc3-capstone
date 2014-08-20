# Practical Assignment
# Question 2

print("Enter the hours:",end="\n")
hours= eval(input())
print("Enter the minutes:",end="\n")
minutes= eval(input())
print("Enter the seconds:",end="\n")
seconds= eval(input()) 
if 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
    