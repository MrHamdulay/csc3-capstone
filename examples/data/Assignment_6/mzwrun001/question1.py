"""Program to print a list of names
Runako muzwidzwa
23/04/2014"""

names=input("Enter strings (end with DONE):\n")
name_list=[]

while names!= "DONE":
    name_list.append(names)
    names=input()
print()
print("Right-aligned list:")


length=0
for name_lin in name_list:
    if length<len(name_lin):
        length = len(name_lin)
    else:
        continue

for name in name_list:
    space=(length-len(name))
    print(" "*space,name,sep="")    
