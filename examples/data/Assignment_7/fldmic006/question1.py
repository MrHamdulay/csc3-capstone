#Code to select unique strings from a list
#Michael Field
#27 April 2014

#declare variables
words = []
Input = ""

#ask for input
Input = input("Enter strings (end with DONE):\n")
words.append(Input)

while Input != "DONE":
    Input = input("")
    #add input to the list of words
    if Input not in words:
        words.append(Input)
    
#remove DONE from list
words.remove("DONE")

print("")

#output unique list
print("Unique list:")  

for i in words:
    print(i)
        