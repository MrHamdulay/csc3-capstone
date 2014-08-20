#Mbongeni Mazibuko
#MZBMBO002
#Assignment 6

def right_align():
    #function where the user can enter a list of strings followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.
    print('Enter strings (end with DONE):')
    lName= []
    length= 0
    name=' '
    
    while name!='DONE':
        #get names
        name= input()
        if len(name)>length:
            length= len(name)
        if name!="DONE":
            lName.append(name)
    print()
    print('Right-aligned list:')
    for i in range(len(lName)):
        #print aligned names
        print("{0:>{lenName}}".format(lName[i], lenName=length))
        
if __name__=='__main__':
    right_align()