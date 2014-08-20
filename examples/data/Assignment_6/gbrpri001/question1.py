"""PRIYANKA GOBERDHAN
RIGHT ALLIGN 
25/04/2014"""

print("Enter strings (end with DONE):\n")
names_list=[]
a=""

while(a!="DONE"):
    a=input()
    names_list.append(a)
names_list.remove("DONE")
max=0   
for i in names_list:
    if(len(i)>max):
        max=len(i)

print("Right-aligned list:")
for i in names_list:
    print(" "*(max-len(i)),i,sep='')