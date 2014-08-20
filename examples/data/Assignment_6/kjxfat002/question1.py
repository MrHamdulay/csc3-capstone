'''this program stores a list of inputs and aligns them all along the right side 
fathima zahra kajee
kjxfat002
21 april 2014'''

list=[]
x=input("Enter strings (end with DONE):\n",) 
list.append(x)

while x!="DONE": #inputs in list will continue to be added to list until user types DONE
    x=input("")
    list.append(x)

max=len(list[0])
for k in range(len(list)):
    
    if max<len(list[k]): #find the longest string in order to determine spaces to add before printing string
        max=len(list[k])
    elif max>len(list[k]):
        max=max
print("")
print("Right-aligned list:") #print enough spaces and the string such that it is perfectly against the right margain 

for j in list:
    spaces=" "*(max-len(j)) #print enough spaces and the string such that it is perfectly against the right margain followed by the longest string
    if j!="DONE":
        print(spaces+j)
    
        
