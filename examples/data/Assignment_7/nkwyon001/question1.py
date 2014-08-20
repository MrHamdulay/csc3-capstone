"""program to printout a orded unique list
yondela nkwali
28 April 2014"""

#ask for a list of strings
Lstrings=[]
strings=input("Enter strings (end with DONE):\n")
#put string in the list
while strings != "DONE":
     Lstrings.append(strings)
     strings=input("")
if strings == "DONE":
     print("\nUnique list:")
     Lstrings=list(set(Lstrings)) #delete any duplicates
     Lstrings.sort() #put list in order
     #print out the list
     for astring in Lstrings:
          print(astring)