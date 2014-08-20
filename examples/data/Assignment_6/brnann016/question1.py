"""Program to right-align a list of strings
Annika Brundyn
24/04.2014"""

#Get input from user and create a list
print("Enter strings (end with DONE):\n")
list1=[]
string=input("")
while string!="DONE":
    list1.append(string)
    string=input("")

#find the longest string
longest=0
for i in list1:
    if len(i)>longest:
        longest=len(i)

#Right-align
print("Right-aligned list:")
for i in list1:
    x = i.rjust(longest)
    print(x)
