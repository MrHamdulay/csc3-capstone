"""enter a list of names, and print them out (right-aligned)
Tim Hardie
23-4-14"""

if __name__ == '__main__':
    
    #user inputs names and ends with sentinel value of DONE
    name_in = input ("Enter strings (end with DONE):\n")
    names_list = []
    while (name_in != 'DONE'):
        names_list.append (name_in)
        name_in = input()
    
    #calculate length of longest name
    max_len = 0
    for name in names_list:
        if (len(name) > max_len):
            max_len = len(name)
    
    #print right-aligned list of names
    print ("\nRight-aligned list:")
    str = "{0:>" +str(max_len) +"}"
    for name in names_list:
        print (str.format (name))