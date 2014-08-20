'''programme to print unique list
Siphesihle Zwane 
30 April 2014'''
list1=[]
faka=""
print("Enter strings (end with DONE):"'\n') 
while faka != "DONE":
    faka=input()
    list1.append(faka) #creating a new array
    if faka=="DONE":    #getting rid of done
        list1.remove("DONE")
print("Unique list:")    

list2 = []    
for i in list1:    
    if not i in list2:   #printing each item in list 
        list2.append(i)   
for i in range (len(list2)):
    
    print(list2[i])