#Kalind Ramnarayan
#23 April 2014
#Right aligning strings in a list


list=[]                                            #Create a list
string=input("Enter strings (end with DONE):\n")
while string!="DONE":                               # add strings to the list
    list.append(string)
    string=input()

longest=""                                     #search for the longest string
for i in list:
    if len(i)>len(longest):
        longest=i
print()
print("Right-aligned list:")                   #print out the strings right alligned
gap=" "
for j in list:
    print(gap*(len(longest)-len(j)),j,sep="")
    