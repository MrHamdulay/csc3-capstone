#program to print out strings from user
# Alexander Brunette
# 25/04/2014
    
    
names=input("Enter strings (end with DONE):\n") #get strings
names_list=[] #empty list
while not names == "DONE":
    names_list.append(names) #add strings to list
    names=input("")
        
    
            
max_char=0 #initiate to 0
for j in names_list: #find longest string
    if (len(j))>(max_char):
        max_char=len(j)
            
print("")
print("Right-aligned list:")
for i in names_list: #print each string in list
    print(i.rjust(max_char)) #print adjusted rightwards
   