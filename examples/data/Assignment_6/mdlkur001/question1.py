"""Programe to enter a list of names
Kureshlen Moodley
MDLKUR001
23 April 2014"""

#create an empty list
strings=[]

#get a list of names
string=input("Enter strings (end with DONE):\n")
while string !="DONE":
    strings.append(string)
    string=input("")
x=0
#arrange names to be right-aligned
for string in strings:
    y=len(string)
    if y>x:
        x=y
#print out string        
print("\nRight-aligned list:")
for string in strings:
   
    print(" "*(x-len(string)),string, sep="")
    

