#Rorisang Moseli
#Assignment 6
#Question 1


names = []
print ("Enter strings (end with DONE):")

while True:
    
    
    name = input("")
    
    
    if name == 'DONE':
            break
        
    names.append(name)
        
print ("")        
print ("Right-aligned list:")        
for i in names:
    col_width = len(max(names, key=len))
    print (i.rjust(col_width))