#program to print a list of strings right alligned
#Anthony Jacob
#21 April 2014

#defining the function
def strings():   
    print("Enter strings (end with DONE):\n")
    
    inp=""
    names=[]
    while inp != "DONE":              #loop to stop entering names after 'DONE'
        inp=input("")
        if inp!="DONE":
            names.append(inp)
    print("Right-aligned list:")
    
    longest=0                         
    for nam in names:
        if len(nam)>longest:
            longest=len(nam)
    
    for nam in names:                  #formating names to be right allinged
        print(("{0:>"+str(longest)+"}").format(nam))
            

strings()      #calling fuction