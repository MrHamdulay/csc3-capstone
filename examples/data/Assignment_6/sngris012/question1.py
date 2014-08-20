#Rishen Singh SNGRIS012
#Question One Assignment 6
strings=[] #defines an empty list

print("Enter strings (end with DONE):") 
x=""
while x!="DONE":  #continues to expect string to be inputted while it isn't DONE
    x=input() #input each string into list
    strings.append(x)#adds string to list
strings.remove("DONE")

maxLength=0 #defines variable maxLength to 0
for i in range(len(strings)): #iteration through every item in list
    if(len(strings[i])>maxLength): #if length is greater than maxLength, it reassigns that value to maxLength
        maxLength=len(strings[i])
    else:
        maxLength=maxLength
print()
print("Right-aligned list:")
for i in range(len(strings)): #iteration through every item in list
    spaces= maxLength-len(strings[i]) #calculates the number of spaces in order to align list
    print(" "*spaces+strings[i])