"""Program that prints out a list of strings right-aligned. Input from user.
   Bridgette Lefatsa
   LFTNTO002
   24 April  2014"""

#Get list from user
names=[]
name=input("Enter strings (end with DONE):\n")
if name=="DONE":
    print("\nRight-aligned list:\n")
else:   
    while name !="DONE":
        names.append(name)
        name=input("")

    #Find longest string-
    longest=names[0]
    for x in names:
        if len(x) > len(longest):
            longest=x
        
    #Print right-aligned list
    width=len(longest)
    print("\nRight-aligned list:")
    for k in names:
        print(k.rjust(width))