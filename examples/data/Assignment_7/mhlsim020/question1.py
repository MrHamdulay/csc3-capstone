
mylist=[]
list_strings = []

strings=input("Enter strings (end with DONE):\n")

while strings != "DONE" and strings != "done":
              list_strings.append(strings)
              strings=input()
              for x in list_strings:
                            if x not in mylist:
                                          mylist.append(x)
                                          
                                          
print("\nUnique list:")
print('\n'.join(mylist))                           
              

             
              

                     

