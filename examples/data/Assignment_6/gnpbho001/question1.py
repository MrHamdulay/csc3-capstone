#Programe to enter a list of names
#gnpbho001@UCT ACTSCI


strings=[]


string=input("Enter strings (end with DONE):\n")
while string !="DONE":
    strings.append(string)
    string=input("")
x=0

for string in strings:
    y=len(string)
    if y>x:
        x=y

print("\nRight-aligned list:")
for string in strings:
   
    print(" "*(x-len(string)),string, sep="")
    

