"""Enter and print list of strings
Michelle Lu
19 April 2014"""

#create list
list1=[]
#enter the strings
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
    list1.append(string)
    string=input("")

print("")
print("Right-aligned list:")

#to find the longest length
x=0
for i in list1:
    length=len(i)
    if length>x:
        x=length

#print out results
for j in list1:
    print(" "*(x-len(j)), j, sep="") #multiply spaces with max length-length of the word

    