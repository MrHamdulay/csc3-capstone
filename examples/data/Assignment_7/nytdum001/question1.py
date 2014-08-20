"""Program to remove duplicated items from list
Dumisani J Nyathi
27-04-2014"""

def list_manipulation():
    x=input("Enter strings (end with DONE):\n")
    y=[x]
    while x!="DONE":
        x=input()
        if x in y:
            continue#will automatically remove duplicates from list
        else:
            y.append(x)#if list item apperaing for the first time it will be appended to the list
    print()#blank line
        
    print("Unique list:")
    for i in y:
        if i=='DONE':
            continue
        else:
            print(i)
        
        
list_manipulation()