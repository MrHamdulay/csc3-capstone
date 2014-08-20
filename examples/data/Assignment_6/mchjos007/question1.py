#code for entering strings and right-orientating them josh michelson 22/04/2014#
userenter=input("Enter strings (end with DONE):\n")
listofnames = []
longestlength= 0
while userenter != "DONE":
    if len(userenter) > longestlength:
        longestlength = len(userenter)
    listofnames.append(userenter)
    userenter=input("")
print("")
print("Right-aligned list:")
for a in listofnames:
    print(" "*(longestlength-len(a))+a)