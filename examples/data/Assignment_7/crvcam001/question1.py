# question1.py
# prints out list in the order that the user entered it but without duplicates
# camilla craven
# 28 april 2014


string = input("Enter strings (end with DONE):\n")

List = []

while string != "DONE": # creating sentinel loop (will end when user enters "DONE")
   
    # to avoid duplicates, only add string not already in list    
    if string not in List:
        List.append(string)  
   
    # if string already in list, it is not added
    else: 
        None
   
    string = input() # prompts user for more strings
    
    
print()
print("Unique list:")

# print every string in list (in order)
for i in List:
    print(i)
