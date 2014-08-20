#Ikhlaas Pohplonker
#23 April 2014
#a program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string
lst=[]
string=input("Enter strings (end with DONE):\n")
while string != "DONE":#asks user to enter a string until the user enters DONE
    lst.append(string)#adds each string entered to the list called lst
    string = input()
    
print()
maximum=0
for i in lst:#iterate through list to find word with the maximum length
    if len(i)>maximum:
        maximum=len(i)
print("Right-aligned list:")
for i in lst:#print right aligned list of the words in lst
    z = ("{0:>" + str(maximum) + "}").format(i)
    print(z)    
    
    
    