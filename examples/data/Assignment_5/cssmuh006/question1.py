
choice=""
message=""
fileList=["42.txt","1015.txt"]
life=open('42.txt','r').read()
Comp=open('1015.txt','r').read()
files=[life,Comp]

while(choice!='X'):
    choice=input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n").upper()
    
    if(choice=="E"):
        
        message=input("Enter the message:\n")
        
    elif(choice=="V"):
        
        if(len(message)==0):
            print("The message is: no message yet")
        else:
            print("The message is:", message)
            
            
    elif(choice=="L"):
        
        print("List of files: ",end="")
        l=""
        for i in range (len(fileList)):
            if(i!=len(fileList)-1):
                l=l+str(fileList[i])+", "
                
            else:
                l=l+str(fileList[i])
                
        print(l)
        
    elif(choice=="D"):
        
        nameF=input("Enter the filename:\n")
        found=False
        
        for i in range (len(fileList)):
            
            if(nameF==fileList[i]):
                found=True
                print(files[i])            
                
        if(found==False):
            print("File not found")
            
    else:
        print("Goodbye!")