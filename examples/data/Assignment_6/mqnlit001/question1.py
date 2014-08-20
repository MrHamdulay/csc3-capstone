#Assignment 6: Question 1
#Program to right align the inputted data
#Author: Litha Maqungo

instruction= input(("Enter strings (end with DONE): \n")) #the input for the program
string_names=[] #emptylist for the strings to be input
while instruction != "DONE": #looping it until it terminates with DONE
    string_names.append(instruction) 
    instruction=input()
print()
maxlength=0
for i in string_names: #ascertaining the length of the longest string
    if len(i)>maxlength:
        maxlength = len(i)
print("Right-aligned list:")

for j in string_names: #calculating the spaces needed
    print(" "*(maxlength- len(j)),j,end=" ",sep="")
    print()
    
