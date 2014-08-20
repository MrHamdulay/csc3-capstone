"""Program to print a supplied list excluding duplicates.
Kemeshan Naicker
28 April 2014"""

def uni_list():
    #Prompt user for list.
    print("Enter strings (end with DONE):")
    item = input()
    itemlist = []
    while item != "DONE":
        itemlist.append(item)
        item = input()
    #Remove duplicates from list.
    newlist = []
    for i in itemlist:
        if i not in newlist:
            newlist.append(i)
    #Print the new list.
    print("\nUnique list:")
    for i in newlist:
        print(i)
        
if __name__=="__main__":
    uni_list()
            
    