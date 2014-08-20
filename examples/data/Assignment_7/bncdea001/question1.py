#Program to print a list of unique names
#27 April 2014
#Dean Bunce

#Create empty list
entry_names=[]

# Get input

print("Enter strings (end with DONE):\n")

#Priming statement for names
names=""


#Get input 
while names !="DONE":
    
    #Ask for input
    names=input("")    
    #Add new names and not old ones
       
    if names not in entry_names and names!="DONE": 
        entry_names.append(names)    
    
    else: continue
    
    
    
    
   
    

#Print the names out    

print("Unique list:")
for names in entry_names:
    print(names)
    