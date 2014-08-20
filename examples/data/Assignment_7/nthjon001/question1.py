"""Prints list of strings in the same order that the user entered them in, but deletes any duplicates
Jonathan Nathan
27 April 2014"""
 
def main():
    string_list = []
    # user enters a string
    input_word = input("Enter strings (end with DONE):\n")
    # appends unique input to string_list until the sentinel, "DONE", is input
    while input_word != 'DONE':
        if input_word not in string_list:
            string_list.append(input_word)
        input_word = input('')
    
    print()
    print("Unique list:")
    # prints the unique strings in the same order they were inputted as
    for word in string_list:
        print (word)
    
if __name__ == '__main__':
    main()