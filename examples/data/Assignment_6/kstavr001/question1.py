#Assignment 6
#Question 1
#Avreyna Kistensamy
#20 April 2014

#Get list from user
Str = []
x=input("Enter strings (end with DONE):\n")
while x != "DONE":
    Str.append (x)
    x= input("")
    
length=0
for string in Str:
    str_length = len(string)
    if str_length > length:
        length=str_length

#Create loop to R-justify all the names
justified = []
for string in Str:
    r_just = string.rjust(length)
    justified.append(r_just)
    
#print out right justification
print()
print("Right-aligned list:")
for string in justified:
    print(string)