#Gina Horscroft, Assignment 7
#Question1

unique_list = []
st = input("Enter strings (end with DONE):\n")
while (st != "DONE"):
    if (st not in unique_list):#checks if string has been entered before
        unique_list.append(st)#if unique, adds to list
    st = input("")    
print("\nUnique list:")
for i in unique_list:
    print(i)