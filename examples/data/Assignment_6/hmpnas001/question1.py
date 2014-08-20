"""program to print names right aligned
nasonkwe hampwaye
2014-04-24"""
#input strings
names=[]
name_input=input("Enter strings (end with DONE):\n")
while name_input!="DONE":
    names.append(name_input)
    name_input=input("")
#get longest name   
max_len=0
for i in range(len(names)):
    if len(names[i])>max_len:
        max_len=len(names[i])
       
#align
print("\nRight-aligned list:")
for i in names:
    print(" "*(max_len-len(i)),i,sep="")