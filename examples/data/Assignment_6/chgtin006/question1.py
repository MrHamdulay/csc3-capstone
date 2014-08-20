"""Program to right align members of a list
By Tinashe Choga
25/05/201a"""
#creating the empty list
name=[]
names=input("Enter strings (end with DONE):\n")
#adding input to the list
while names != "DONE":
    name.append(names)
    names=input("")

print('\n'"Right-aligned list:")
a=0
#measuring length of longest word
for i in name:
    if len(i)>a:
        a=len(i)
#printing right aligned list
for n in name:
    print(" "*(a-len(n))+n)
        

    
    
    

    