#Jono Field
#1 May 2014
#Question 1.pu 

Str = input("Enter strings (end with DONE):\n") #prompts user to enter strings
list = []


while Str != "DONE":  #sentinel loop is created
    if Str not in list:
        list.append(Str)   #add string if it is not already in list
        
    else:
        None
    Str=input()  #prompts user to enter more strings

print()
print("Unique list:")

for j in list:
    print(j)   #prints every string in the list
    