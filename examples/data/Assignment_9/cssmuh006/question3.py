"""Check if a sudoku grid is valid
Haaroon Cassiem
11 May 2014"""
def getSudoku(f):
    #get input ad make it a list
    suds=[]
    try:
        load=open(f,"r")
        l=load.read()
        suds=l.split("\n")        
    except:
        suds=f.split("\n")
    
    return suds

def checkValid(l):
    valid=True
    #check rows and columns for validity
    for i in range(len(l)):
        for j in range(len(l[i])):
            r=l[i][j]
            c=l[j][i]
            for k in range(len(l[i])):
                if (k!=j and r==l[i][k]):
                    valid=False
                elif(k!=j and c==l[k][i]):
                    valid=False
    #check 3x3 grids in list
    for j in range(0,6,3):
        for i in range(0,6,3):
            for y in range(0,3):
                for x in range(0,3):
                    for q in range(y+1,3):
                        for p in range(x+1,3):
                            if(l[j+y][i+x]==l[j+q][i+p]):
                                valid=False                            
    return valid

if __name__=="__main__":
    f=""
    while(len(f)<81):
        f=f+input()+"\n"
    num=getSudoku(f)
    v=checkValid(num)
    if v:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")