'''Sanele Mdlalose
   MDLSAN019
   01-05-2014
   List of strings that have no duplicates'''

def strings():
        #inputs a list of strings
        strings=input("Enter strings (end with DONE):\n")
        string_list=[]

        if strings!='' and strings!='DONE':
                while True:
                        while not strings in string_list:
                                string_list.append(strings)
                        
                        strings=input("")
                                
                        if strings=='DONE':
                                print()
                                break
        
        else:
                print()   

        print("Unique list:")
        for i in string_list:
                #list display
                print(i)
#function call
strings()        