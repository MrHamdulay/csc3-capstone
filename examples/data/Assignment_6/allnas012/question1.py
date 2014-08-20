def main():
    #mylist=[]
    #x=input("Enter strings (end with DONE):\n")
    #while x !="DONE":
        #x=input("")
        #mylist.append(x)
        #for x in mylist:
            #return mylist
    #print("Right-aligned list:\n {0:>5}".format(mylist))
    
    mylist=[]
    
    x = input ("Enter strings (end with DONE):\n")
    while x != 'DONE':
        mylist.append(x)
        x = input("")
    
    print("\n""Right-aligned list:")
    for x in mylist:
        maximum = max(mylist, key=len) 
        new_maximum = len(maximum) 
        diff = new_maximum - len(x)
        title = diff*' '
        print(title+x)     

  
    

main()