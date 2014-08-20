def align():
   
    strings = input("Enter strings (end with DONE):\n")
    
    
    list_str = [strings]

    
    while strings != "DONE":
        strings = input()
        list_str.append(strings)
    
    list_str.remove("DONE")
    string_max = 0 #
    for x in range(len(list_str)):
        if len(list_str[x]) > string_max:
            string_max = len(list_str[x])
        
    print()
    print("Right-aligned list:")
        
       
    for y in range(len(list_str)):
        print(list_str[y].rjust(string_max))
        
align()