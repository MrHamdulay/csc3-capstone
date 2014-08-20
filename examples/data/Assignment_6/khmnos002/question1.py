"""program that right aligns a list of names
nosipho khumalo
19 April 2014"""

def main():
    
    #creating a list
    list = [] #creates list as the names are entered
    
    name = input("Enter strings (end with DONE): \n")
    while name != "DONE":
        list.append(name)
        name = input("")
    
    print("")
    print("Right-aligned list:")        
    
    #finding length of longest string
    if len(list) > 0:
        max = len(list[0])
        if len(list) > 1:
            for i in (1,len(list)-1):
                if len(list[i]) > max:
                    max = len(list[i])
       
    #print out the list of names right aligned with longest string 
        for name in list:
            new_name = "{0:>{1}}".format(name, max)
            print(new_name)
main()