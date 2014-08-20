
'''this program stores a list of names and aligns them all along the right side 
quincy cele
21 april 2014'''
list=[]
x=input("Enter strings (end with DONE):\n",)
list.append(x)
#user must continue to add the words into the list until user types DONE
while x!="DONE":
    x=input("")
    list.append(x)
#we must find the longst word inorder to figure out the amount of spaces we should add before printing the actual word
max=len(list[0])
for k in range(len(list)):
    
    if max<len(list[k]):
        max=len(list[k])
    elif max>len(list[k]):
        max=max
print("")
print("Right-aligned list:")
#now we print  enough spaces and the word such that it is perfectly against the right margain dictated by the longest word
for j in list:
    spaces=" "*(max-len(j))
    if j!="DONE":
        print(spaces+j)
    
        
