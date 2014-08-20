"""Assignment 6, Question 1
Yaseen Sulliman
20 April 2014"""

list_=[] # creating list
string=input("Enter strings (end with DONE):\n") # asking user  for strings within list
list_.append(string) # adding string to list
while string!="DONE":
    string=input("")
    list_.append(string) # adding string to list
    
# finding the length of longest string in the list
p=0
for item in list_:
    if(len(item)>p):
        p=len(item)
print("")
print("Right-aligned list:")
# printing list with right alignment        
for i in range(0, len(list_)-1):
    print(list_[i].rjust(p))



