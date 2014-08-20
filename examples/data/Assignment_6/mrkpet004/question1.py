"""program to pring out a list of previously entered strings in order of length
peter m muriuki"""

string=input("Enter strings (end with DONE):\n")
s=[]  
m=[]
#get list of names and add into an array
while string !="DONE":
    s.append(string)
    string=input("")
    
#print out the list in a right aligned format
print ("\n"+"Right-aligned list:")
if s!=[]:
    for i in s:
        m.append(len(i))
    top=max(m)
    for i in s:
        gap=top-len(i)   
        print (" "*gap+i)      