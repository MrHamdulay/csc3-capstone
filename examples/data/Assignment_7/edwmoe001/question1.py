def cleaner(array):   
    checked = []
    for e in array:
        if e not in checked:
            checked.append(e)
    return checked


def main():
    string_list = []
    name =""
    print("Enter strings (end with DONE):")
    #while loop to add values to list
    while name != "DONE":
        name = input()
        string_list.append(name)
    del string_list[-1]    
    print()
    print("Unique list:")
    clean = cleaner(string_list)
    for i in range(len(clean)):
        print(clean[i])
        
main()