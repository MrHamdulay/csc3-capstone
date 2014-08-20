def options():
    options=(((input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n"))[0]).upper())
    return(options)

def create(sel):
    mes="no message yet"
    if sel=="E":
        mes=input("Enter the message:\n")
    return(mes)
    
def filey(sel):
    dl="File not found"
    al="42.txt"
    bl="1015.txt"
    a="The meaning of life is blah blah blah ..."
    b="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
    if sel=="L":
        dl="42.txt, 1015.txt"
        #return(dl)
    if sel=="D":
        filesel=input("Enter the filename:\n")
        if filesel==al:
            dl=a
        elif filesel==bl:
            dl=b
        else:
            dl="File not found"
    if sel=="F":
            dl="File not found"
    return(dl)
        
    

def BBS():
    sel=options()
    if sel=='Syntax Error':
        print("fuck you")
    ThisIs=1
    SoDamCool=1
    mes=create("V")
    disp=filey("F")
    if sel=="X":
        print("Goodbye!")
        ThisIs=4
    while ThisIs==SoDamCool:
        while sel=="E" or sel=="V":
            if sel=="V":
                print("The message is:",mes)
            if sel=="E":
                mes=create(sel)
            sel2=options()
            if sel2=="X":
                sel=sel2
                break            
            if sel2==sel:
                sel=sel2
            elif sel=="E" and sel2=="V":
                #print("The message is:",mes)
                sel=sel2
            elif sel=="V" and sel2=="E":
                mes=create(sel)
                sel=sel2
            elif sel2!="E" or sel2 !="V":
                sel=sel2            
                break
    
        while sel=="L" or sel=="D":
            if sel=="L":
                print("List of files:",filey("L"))
            if sel=="D":
                disp=filey(sel)
                print(disp)
            sel2=options()
            if sel2=="X":
                break
            if sel2=="L":
                sel=sel2
                print("List of files:",filey("L"))
            if sel2=="D":# or sel2=="L":
                sel=sel2
                disp=filey(sel)
                print(disp)
            if sel2!="D" or sel2!="L":
                sel=sel2
                break
        if sel=="X":
            print("Goodbye!")
            break
        while sel!="X" or sel!="V" or sel!="D" or sel!="L" or sel!="E":
            sel2=options()
            sel=sel2
            if sel2=="X" or sel2=="E" or sel2=="D" or sel2=="V" or sel2=="L":
                sel=sel2
                break

BBS()



        

    
