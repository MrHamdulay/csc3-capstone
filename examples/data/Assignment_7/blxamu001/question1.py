"""Program that prints input strings with no duplicates
Aubrey Baloi
27 April 2014"""

def un_dupl():
    strings = [] #list with duplicate strings
    string = input("Enter strings (end with DONE):\n")
    strings2 = []
    
    #if string =='DONE':
        #print('\nUnique list:')
    
    while string != 'DONE':
        strings.append(string)
        string = input()
    
    for i in strings:
        if i not in strings2:
            strings2.append(i)
    
    
    print('\nUnique list:')
    for j in strings2:
        print(j)
        
un_dupl()

 