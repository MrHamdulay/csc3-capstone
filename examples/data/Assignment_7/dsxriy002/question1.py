#Program to print a supplied list excluding the duplicates 
#Riya Desai
#30 April 2014


def uni_list():

#Ask user to type in a list
    print("Enter strings (end with DONE):")
    newentry = input()
    numberinlist = []
    while newentry != "DONE":
        numberinlist.append(newentry)
        newentry = input()
    
    
#Take out the strings in the list that were repeated any number of times
    revisedlist = []
    for i in numberinlist:
        if i not in revisedlist:
            revisedlist.append(i)
            
            
#Print the new list without the duplicates
    print("\nUnique list:")
    for i in revisedlist:
        print(i)
        
if __name__=="__main__":
    uni_list()
            
    