"""get a list of strings and print them out without duplicates
Tim Hardie
1/5/14"""

if __name__ == '__main__':
    #get user input
    input_list = []
    str_in = input ("Enter strings (end with DONE):\n")
    while (str_in != "DONE"):
        input_list.append (str_in)
        str_in = input()
    
    #print unique strings list
    print("\nUnique list:")
    for i in range (len (input_list)):
        #checks if string at index i has appeared in the list already
        if input_list[i] not in input_list[:i]:
            print (input_list[i])