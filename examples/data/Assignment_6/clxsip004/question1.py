#Siphesihle Cele
#26 April
#Program that takes in a string, the prints it in a right angle triangle.
#using a while loop for the names until done is entered
#then for loop need to print one below the other.


def string_align():
    name_list = []
    string_lens = []
    string_enter = input("Enter strings (end with DONE):\n")
    name_list.append(string_enter)
    while string_enter != 'DONE':
        string_enter = input()
        name_list.append(string_enter)
    z = name_list.index('DONE')
    del name_list[z]
    for name in name_list:
        x = len(name)
        string_lens.append(x)
    string_lens.sort()
    print()
    print("Right-aligned list:")
    if len(string_lens)>0:
        align = string_lens[-1]
        
        
        for name in name_list:  
            print((align-len(name))*' ', name,sep = '')
string_align()