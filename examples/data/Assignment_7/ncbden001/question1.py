#Program to diplay unique list
#Denzel Ncube
#28 April 2014

#Setting variables
uniquelst = []
lst = []
strings = ""
stringlst = ""

#Getting input
print("Enter strings (end with DONE):\n")

while strings != "DONE":
        strings = input()
        lst.append(strings)

#Deleting done
del lst[-1]

#Putting all the unique words into a string then back into a list
for i in range(len(lst)):
        if lst[i] not in stringlst:
                stringlst += lst[i]+ ' '
uniquelst = stringlst.split(" ")

#Printing output
print("Unique list:")
for i in range(len(uniquelst)):
        print(uniquelst[i])


       