# a Python program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
# mashau zwivhuya
# 28 april 2014
def main():
    # creating empty list
    list1=[]
    # getting input from user 
    strings=input("Enter strings (end with DONE):\n")
    list1.append(strings)
    # adding strings to list
    while strings !="DONE":
        strings=input("")
        if strings in list1:
            continue
        else:
            list1.append(strings)
    # removing DONE        
    for i in list1:
        if i =="DONE":
            list1.remove(i)
    #printing out the output        
    print()        
    print("Unique list:")
    for i in list1:
        print(i)
    
main()    
            