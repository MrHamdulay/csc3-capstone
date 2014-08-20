"""Program to print out strings right aligned
Thiloshni Moodley
22 April 2014"""

lengths=[]
strings=[]
string=input("Enter strings (end with DONE):\n")
while string != "DONE":
    strings.append(string)
    string=input("")
    
print("\nRight-aligned list:")

for j in range(len(strings)):
    leStrings =(len(strings[j]))
    lengths.append(leStrings)
    
max_length = 0
for a in range(len(lengths)):
    if lengths[a]>max_length:
        max_length = lengths[a]

for o in range(len(strings)):
    len_name = max_length - (len(strings[o]))
    print(" "*len_name,(strings[o]),sep="")