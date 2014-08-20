#Riya Desai
#Assignment 6, Question 1
#23 April 2014

       
       
       
entries=input("Enter strings (end with DONE):\n")
    
listofnames=[]
    
maxlength=0
    
while entries != "DONE":
    listofnames.append(entries)
    entries=input("")
        
    if len(entries) > maxlength:
            maxlength=len(entries)
    
print("\nRight-aligned list:")
for entries in listofnames:
    print(entries.rjust(maxlength))