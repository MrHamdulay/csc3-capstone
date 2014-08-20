"""program to make strings right aligned with the longest string in the list
yondela nkwali
20 April 2014"""

#get a list of srings  
Lstrings=[]
strings=input("Enter strings (end with DONE):\n")
#If user inputs DONE 1st
if strings=="DONE":
    print("\nRight-aligned list:\n")
    
#when we get a list to work with
else:
    while strings!="DONE":
        Lstrings.append(strings)
        strings=input("") 
        
    print("\nRight-aligned list:\n",end="")
    #change them to be right-aligned and print it out
    max=max(Lstrings,key=len)
    Lmax=len(max)
    for string in Lstrings:
        Lstring=len(string)
        print(" "*(Lmax-Lstring)+string)