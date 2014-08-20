"""Right-align given string
Christopher Sterley
20/04/2014"""

#Get first input
list_str=input("Enter strings (end with DONE):\n")
output_str=[]

#Create list to be right-aligned
while list_str!="DONE":
    output_str.append(list_str)
    list_str=input("")

#Finding the field width
if len(output_str)>0:
    width=len(max(output_str, key=len))
else:
    width=0

print()

print("Right-aligned list:")
#Print right-aligned list
for i in range(len(output_str)):
    print("{0:>{1}}".format(output_str[i],width))