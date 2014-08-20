#Tato Moaki MKXTAT001
#Program to print unique elements of a list
#Assignment7 question1

def main():
    myString_list = []
    print("Enter strings (end with DONE):")
    
    flag = True
    while flag:
        strings_input = input()
        if strings_input == "DONE":
            flag = False #break out of the loop statement when the sentinel is input
        else:
            myString_list.append(strings_input)
            
    myUnique_list = [] #create an empylist
    for string in myString_list:
        if not string in myUnique_list:
            myUnique_list.append(string) #add elements that have not been added to list only
            
    print("\nUnique list:")
    for j in myUnique_list:
        print(j)
        
if __name__=="__main__":
    main()