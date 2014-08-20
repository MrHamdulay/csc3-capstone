#Thiolan Prevan Naidoo
#NDXTHI031
#question1  
#Print a unique list of strings

strings=[] 
new=[]
x=input("Enter strings (end with DONE):\n") #Stores the first string as variable x

while x!="DONE": #Checks if the variable x is not "DONE"
    
    strings.append(x)#adds the variable x to the list strings
    x=input() #overwrites x and stores the next input as variable x
    
for i in strings: #for loop whereby i takes on each value of the list strings
    if not i in new:#checks if i appears is in the list new and if not it appends x to the list new
        new.append(i)
print()
print("Unique list:")       
for j in new:#prints each item in the list new
    print(j)