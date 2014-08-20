"""Assignment 6 Question 1
Prints out right alligned list of strings
Shaheen Karodia
KRDSHA003
2014-04-02"""

def main():
    
    print("Enter strings (end with DONE):")
    stringlist=[]
    width=0
    x=0
    while x!="DONE":
        x=input("")
        if x=="DONE":
            
            for i in stringlist:  #calculate the length of the longest word
                if len(i)>width:
                    width=len(i)
                
              #justify all strings to  theright 
                    
        else:
            stringlist.append(x)  #add strings to the list
            

    print()
    print("Right-aligned list:")
    if stringlist!=[]:
        for j in stringlist:
            print ((width-len(j))*(" "), j, sep="")
main()

