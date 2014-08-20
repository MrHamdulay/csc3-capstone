"""Program to right-align a list of strings
Joseph Preyer
24 April 2014"""


lis=[]

# Get strings from user and add to list
print("Enter strings (end with DONE):\n")
add=input("")
while add!="DONE":
    lis.append(add)
    add=input("")
    
# Find length of longest string in list
if len(lis)>0:
    length = len(lis[0])
for i in lis:
    if len(i)>length:
        length = len(i)

# Format all words to right align with end of longest string
print("Right-aligned list:")
for i in lis:
    i=" "*(length-len(i))+i
    print(i)
        