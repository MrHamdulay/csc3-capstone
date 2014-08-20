"""making a list of names
Yonela Ford
21 April 2014"""

"""create empty list to be appended"""

def list():
    #CREATE A LIST OF NAMES
    names=[]
    command=input("Enter strings (end with DONE):\n")
    while command !="DONE":
        names.append(command)
        command=input("")
    print()
    #CREATE LIST OF ALL LENGTHS OF LISTS OF NAMES 
    string=[]
    for i in range (len(names)):
        string.append(len(names[i]))
        
    # PRINT LIST OF NAMES RIGHT ALIGNED ACCODING TO LONGEST WORD    
    print("Right-aligned list:")
    for i in names:
        x=max(string)
        y=" "*(x-len(i))
        print(y,i,sep="")
list()
