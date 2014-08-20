# program to enter a list of strings
# by Jacob Mwanza
# 23/04/2014


def entry():
    string_list = []
    longest_word = 0
    # enter the string list
    enter_list = input('Enter strings (end with DONE):\n')
    while enter_list != 'DONE':
        string_list.append(enter_list)
        enter_list = input()
        
    # find longest word
    for i in range(len(string_list)):
        if len(string_list[i]) > longest_word:
            longest_word = len(string_list[i])
        
        
    # print contents of string_list
    print()
    print("Right-aligned list:")
    
    for j in range(len(string_list)):
        formattedstring = ('{:>'+str(longest_word)+'}')
        print(formattedstring.format(string_list[j]))
    
entry()        
