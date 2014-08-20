"""Program to print a list excluding duplicates
thushar hariparsad
28 April 2014"""

def uni_list():
    #Prompt user for list
    print("Enter strings (end with DONE):")
    item = input()
    list1 = []
    while item != "DONE":
        list1.append(item)
        item = input()
    #Remove duplicates from list
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    #Print the new list
    print("\nUnique list:")
    for i in list2:
        print(i)
        
if __name__=="__main__":
    uni_list()
            
    