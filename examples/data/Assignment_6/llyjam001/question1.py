"""Assignment 6 Question 1
James Lloyd
21 April 2014"""

#Get names in list
name=input("Enter strings (end with DONE):\n")
list=[]
while not name=="DONE":
    list.append(name)
    name=input()
    
#Iterate through names and determine max length
maximum=0
for i in list:
    x=len(i)
    if x>maximum:
        maximum=x
        
#Iterate through list and print
print()
print("Right-aligned list:")
for i in list:
    a="{0:>" +str(maximum)+"}"
    print(a.format(i))
    