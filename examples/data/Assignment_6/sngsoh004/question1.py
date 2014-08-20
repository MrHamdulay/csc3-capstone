#SNGSOH004
#Assignment 6
#Question 1
#23rd April 2014


print("Enter strings (end with DONE):") #Prompt input
arr = [] #empty array
string = str
length=0

while string!="DONE": #checking to see if the user does not want to quit
    string = input()
    arr.append(string) #adding the string to the array
    if len(string)>length:
        length = len(string) #adjusting the maximum length
print("\nRight-aligned list:")
for j in range(len(arr)-1):
    output = ("{0:>"+str(length)+"}").format(arr[j]) #creating the formatted string to be printed
    print(output)