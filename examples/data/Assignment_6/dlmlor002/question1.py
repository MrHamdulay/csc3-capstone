"""program to right-align a list of strings
Lorena Dal Maso
22 April 2014"""

print("Enter strings (end with DONE):")

#create list of strings
string=input("")
string_list=[string]

while string !="DONE":
        if string=="DONE":
                break
        string=input("")
        if string!="DONE":
                string_list.append(string)

#find string with maximum width
width=(max(string_list, key=len))
width2=len(width)

#print right-aligned list
print("\nRight-aligned list:")
for string in string_list:
        if string=="DONE":
                break
        print(" "*(width2-len(string)),string,sep="")