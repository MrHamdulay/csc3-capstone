name = ""
list_names = [] #turning sting input to a list
names=input("Enter strings (end with DONE): \n")
#list_names=names.split()
list_names.append(names)
while names != "DONE": 
    names = input()            #the whole loop is adding each string as a list value into the main list
    list_names.append(names) 
    

max=0  #so that possible max can be alterd to the max given in the list
for i in range (len(list_names)):
    length=len(list_names[i])     #we use a for loops to change the maximum number but on this line we are changing each list value to their length number
    if length>max:
        max=length
print()        
print("Right-aligned list:")
for j in range(len(list_names)-1):          
    k = len(list_names[j])
    
    print(" "*(max-k),list_names[j],sep="")  #right alignment



#for i in range(len(list_names)):
    #name="{0:>{1}}".format(i,max)
    #print(list_names[name])
    
    
        




