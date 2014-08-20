""" duplicates
Tameryn Pillay
30 April 2014 """

def count (the_list, value):
    
    # code from class
    global counter
    counter = 0
    for item in the_list:
        if item == value:
            counter += 1
    return counter

def main ():
     
    # getting strings
    str_input = input("Enter strings (end with DONE):\n")    
    strings = []
    while str_input != "DONE" :
        strings.append (str_input)
        str_input=input()
    else:
        print("")
        
    # output the unique list    
    print("Unique list:")
    new_list = []
    for word in strings:
        new_list.append(word)
        p = count(new_list, word) # checking to see if word is already in list
        if p > 1:
            pass
        else:
            print(word)
        
main()
    
    
    
