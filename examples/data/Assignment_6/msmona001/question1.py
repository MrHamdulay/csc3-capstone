#program where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.

#Initialize array
arrStrings = []
#Enter strings till word is "DONE"
string = input("Enter strings (end with DONE):\n")
while string.upper() != "DONE":
    arrStrings.append(string)
    string= input("")
    
#get length of space for alignment
Max=0
for k in range(len(arrStrings)):
    if Max < len(arrStrings[k]):
        Max = len(arrStrings[k]) 
#get alignment string
s= "{0:>" + str(Max) + "}"

#print right-aligned
print("\nRight-aligned list:")
for n in range(len(arrStrings)):
    print(s.format(arrStrings[n]))