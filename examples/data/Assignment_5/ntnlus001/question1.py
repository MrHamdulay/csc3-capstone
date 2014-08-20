"""BBS exchange
Luci Ntanjana
15-04-2014"""


#E="Enter a message:\n"
#V="The message is: test message"

#x=eval(input("Enter your selection:\n"))

while True:
    k=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")
    if k=="v":
        print("The message is: no message yet")

    
    

    if k=="E" or  k=="e":
        message=input("Enter the message:\n")
   
        if k == "V" or k=="v":
            print("The message is :",message)
      
    if k=="x":
        print("Goodbye!")
        break
    
    if k=="l":
        print("List of files: 42.txt, 1015.txt")
   
    if k=="d":
        m=input("Enter the filename:\n")
        if m=="42.txt":
            print("The meaning of life is blah blah blah ...")
    
        
        elif m=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
     
        
        else :
            print("File not found")
     
        
        
            
    
        
    

    