'''program to right align a list of names
matshepo masshabela
24 aprril 2014'''
#get list
names_enter=input("Enter strings (end with DONE):\n")
names= [names_enter]

while names_enter!="DONE":
    names_enter=input()
    if names_enter!="DONE":
        names+=[names_enter]

#finding length of a name
counts=[]
maxi=0

#print aligned string
print()
print("Right-aligned list:")
for name in names:
    x=len(name)
    if x>maxi:
        maxi=x
for name in names:
    if name!="DONE":
        print(" "*(maxi-len(name)),name,sep="")
    


              
       