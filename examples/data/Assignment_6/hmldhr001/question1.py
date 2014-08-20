
#Dhriven Hamlall

def main():
    
    names=[] #list
    name=input(("Enter strings (end with DONE):\n"))
    maximum=0 
    
    while name!="DONE":
#=====================================================================        
        if len(name)>maximum:
            maximum=len(name) #getting maximum length
#=====================================================================            
        names.append(name)
        name=input() #adding names to list
#=====================================================================       
    print()
    print("Right-aligned list:")
#=====================================================================   
    for i in names:
        print(i.rjust(maximum))
        #The method rjust() returns the string right justified in a string of length width.

main()