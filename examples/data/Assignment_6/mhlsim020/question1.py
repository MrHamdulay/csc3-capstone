"""a program to print out a list of strings right-aligned with the longest string
Simlindile Mahlaba
23 April 2014"""

def strings_list():
    list_names=[]
    strings = input("Enter strings (end with DONE):\n")
    counter=0
    width=0
    length=0
    while strings != "DONE" and strings!= "done":
        list_names.append(strings)
        counter+=1
        length=len(strings)
        if length>width:
            width=length        
        strings=input("")
        
    print("\nRight-aligned list:")
    for i in range(counter):
        print(list_names[i].rjust(width))


strings_list()







    
    

    

