#Tato Moaki MKXTAT001
#Program accepts a list of strings from user and prints them right aligned
#4/20/2014

def main():    
    string_list = [] #empty list
    flag = False    
    print("Enter strings (end with DONE):")
    
    #loop prompts user for input until done
    while not flag:
        strings_input = input()        
        if(strings_input == "DONE"):
            flag = True
        else:
            #add items to the string_list end to end
            string_list.append(strings_input)        
    if len(string_list) != 0:       
        max_width = (len(max(string_list, key=len))) #find the string with greatest length and assign its length to max_width

    print("\nRight-aligned list:")
        
    for string in string_list:
        #right align the elements of the list padded to maximum width
        print(string.rjust(max_width))     
        
if __name__=="__main__":
    main()

