'''david onyango'''

#Set variables
uniquelst = []
lst = []
string = ""
stringlist = ""

# input
print("Enter strings (end with DONE):\n")

while string != "DONE":
        string = input()
        lst.append (string)

del lst[-1]

#Putting all the unique words into a string then back into a list


for i in range (len (lst) ):
        if lst [i] not in stringlist:
               
                stringlist += lst[i]+ ' '

uniquelst = stringlist.split(" ")

#Printing output
print("Unique list:")

for i in range(len(uniquelst)):
        print(uniquelst[i])


       