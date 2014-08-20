#Gina Horscroft
#Assignment6

arrName = []
names = input("Enter strings (end with DONE):\n")
longest = len(names)
while (names!= "DONE"):
    arrName.append(names)
    names = input("")
    #determine longest word
    if (len(names)>longest):
        longest = len(names)
print("\nRight-aligned list:")        
for i in arrName:
    #print the words with spaces to right align
    print (" "*(longest-len(i)), i, sep = "")
    
