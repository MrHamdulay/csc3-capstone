#MKNNIT002
#Queston 1 ass 6

print("Enter strings (end with DONE):")
name_list=[]     #create empty list
max=0

while (True):
    name=input()  
    if name=="DONE":  #discontinue loop if user enters "DONE"
        break

    else:
        name_list.append(name)  #add strings to the empty list
        if len(name)>=max:
            max=len(name)    #set max to be the length of the longest string
           
for i in (name_list):
    print (i.rjust(max," "))  #print all the values of the list adjusted to the right
        
        
        
    
    