#Joy Arendse-Gorvalla
x=input("Enter strings (end with DONE):\n")

L=[] #creating a list

while x!="DONE": #sentinel loop so will end when DONE is entered
    if x not in L:
        L.append(x) #if the input my user is not in the list it will be added to the list
        
    else: #if x is in the list already it will do nothing and not be added
        None
    
    x = input() #promps for more input until they enter "DONE"
    
print() 
print("Unique list:")

for a in L: #for every word in the list, it will print, in order
    print(a)

