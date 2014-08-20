"""program to print strings with no duplicates
nosipho khumalo
27 April 2014"""

def main():
    list = []
    word = input("Enter strings (end with DONE): \n")
    while word != "DONE":
        list.append(word)
        word = input("")
    
    print("")
    print("Unique list:")
    
    #removing duplicates
    new_list = []
    for word in list:
        if word not in new_list:
            new_list.append(word)
    
    #printing list with no duplicates
    for word in new_list:
        print(word)
main()