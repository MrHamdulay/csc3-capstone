"""program that prompts the user to enter a list of strings 
followed by the sentinel "DONE" and the list of strings is then
printed out right-aligned with the longest string.
Author: Dominic Manthoko
21 April 2014
"""

def strings():
    # prompt the user to enter a list of strings
    strings = input("Enter strings (end with DONE): \n")
    
    # create an empty list where the list of names will be stored
    list_str = []
    
    # while the user has not typed 'DONE', prompt the user to enter more strings
    while strings != 'DONE':
        list_str.append(strings)
        strings= input("")
    

    # find the string with the longest length within list_str and store the 
    # string of maximum in the Max variable
    Max = ""
    for string in list_str:
        if len(string) > len(Max):
                    Max = string
        else:
            continue
        
    Max = len(Max)
                
    print("\nRight-aligned list:")
    
    # print each string on a new line right alined with a width equal to
    # the length of the longest string, Max
    for string in list_str:
        print("{0:>{1}}".format(string,Max))        

if __name__ == '__main__':    
    strings()

    
        
    