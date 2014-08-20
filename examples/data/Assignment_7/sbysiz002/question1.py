def replica():
    """ This program accepts a list of string and returns a string without replication"""
    String = input("Enter strings (end with DONE):\n")
    Dictionery = []
    Temp_dict = []
    
    while String != 'DONE':
        Dictionery.append(String)
        String = input('')
        
        if String not in Temp_dict and String != 'DONE':
            Temp_dict.append(String)
    print('')
    print('Unique list:')
    for i in range(len(Temp_dict)):
        print(Temp_dict[i])
replica()    