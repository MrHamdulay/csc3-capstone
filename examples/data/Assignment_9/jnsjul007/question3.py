#Assignment 9 question 3
#Julian van Rensburg
#16 May 2014


#create grid
def main():
    x=''
    y=[]
    for i in range (9):
        x=input("")
        y.append(x)
    
 #create empty variables and check if rows == 45   
    z=0
    a=0
    for item in range(9):
        z=0
        for value in range(9):
            z+= eval(y[item][value])
            if z==45:
                a+=1
    if a !=9:
        print("Sudoku grid is not valid")
    #check if columns ==45    
    else:
        a=0
        for item in range(9):
                z=0
                for value in range(9):
                    z+= eval(y[value][item])
                    if z==45:
                        a+=1
        if a !=9:
            print("Sudoku grid is not valid")  
        #check first sub-grid, if !=45, then not valid    
        else:
            a=0
            for item in range(3):
                
                            z=0
                            for value in range(3):
                                z+= eval(y[value][item])
                            a+=z
            if a!=45:
                print("Sudoku grid is not valid")
                
            else:
                print("Sudoku grid is valid")
                
                                               
        
main()