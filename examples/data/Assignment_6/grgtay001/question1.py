"""program to create a right-aligned list
tayla george
23 april 2014"""


print("Enter strings (end with DONE):")

maxlength =0
string = input()
strings = []
strings.append(string)
    

while string != "DONE":
    string=input()
    strings.append(string)
    
strings.remove("DONE") #deleting done from the list of strings
    

for i in strings:
    if maxlength < len(i):
        maxlength = len(i)
print()        
gap = 0
print("Right-aligned list:")
for j in strings:
    gap =maxlength-len(j)
    print(' '*gap,j,sep='')
    
    
    
    