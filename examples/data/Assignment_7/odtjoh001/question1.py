"""Program to print a list of strings without duplicates
John Odetokun ODTJOH001
27 April 2014"""

olist = []
strings = input("Enter strings (end with DONE):\n")
while strings != "DONE":
    olist.append(strings)
    strings = input()
   

nlist = []
for j in range(len(olist)):
    if olist[j] not in nlist:
        nlist.append(olist[j])
    
        
print("\nUnique list:")
for i in range(len(nlist)):
    print(nlist[i])