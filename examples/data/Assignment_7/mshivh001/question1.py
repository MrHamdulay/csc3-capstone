#MAISHA IVHA
#28/04/2014
#A programme that get list of strings from user and print them out without duplicates

def main():
    #An empty list that will store strings from user
    lst=[]
    lst2=[]
    strng=input("Enter strings (end with DONE):\n")
    while strng!="DONE":#a loop that keeps iterating until a sentinel "Done" is entered
        
        lst.append(strng)#adding a new string to the list
        strng=input("")# an input statement that keeps a user loading the strings
    #print(lst)

    for i in lst:#entering the characters of the first list to the loop
        if i not in lst2:#using control structure to check if the character in list1 is already in list 2
            lst2.append(i)#appending the charactern form list 1 if it is not in list 2
        else:
            pass
    print("\nUnique list:")
    for j in lst2:
        print(j)
             
main()