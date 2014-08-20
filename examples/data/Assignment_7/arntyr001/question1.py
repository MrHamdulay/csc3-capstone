def string_print():
    string_in = input("Enter strings (end with DONE):\n")
    string_list = []
    unique_list = []
    if string_in == "DONE":
        pass
    else:    
        string_list.append(string_in)
        unique_list.append(string_in)
    
    while string_in != "DONE":
        string_in = input()
        if string_in == "DONE":
            break
        else:
            string_list.append(string_in)
    print()
    print("Unique list:")
    
    for i in range(len(string_list)):
        if string_list[i] in unique_list:
            continue
        else:
            unique_list.append(string_list[i])
    for j in range(len(unique_list)):
        print(unique_list[j])
                     
            
string_print()