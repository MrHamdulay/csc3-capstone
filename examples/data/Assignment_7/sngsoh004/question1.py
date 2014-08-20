#Soham Singh
#SNGSOH004
#Assignment 7
#Question 1



arr = [] #empty array
string = ""
print("Enter strings (end with DONE):") #prompting input
while string!="DONE":
    string = input() #storing the input
    if string=="DONE": #if the input is not DONE (the user
        break
    elif string not in arr:
            arr.append(string) #if the item does not exist in the array

print("\nUnique list:")
for i in range (len(arr)):
    print(arr[i])