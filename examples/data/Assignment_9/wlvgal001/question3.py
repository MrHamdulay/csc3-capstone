"""Question 3: Sudoku Checker
Galya Wolov
16 may 2014"""



#creates an empty grid then appends in the input into the sudoku an empty sudoku list
sudoku=[]
inputted=input()
sudoku.append(inputted)
for i in range(8):
        numbers=input()
        sudoku.append(inputted) #makes the 2d array of inputs

#This is a important variable that as soon as it becomes false, the entire program breaks and prints invalid
validity=True

def rowcheck(sudoku):
        counter=0 #checks if greater than 1 at any point there are two values the same and prints invalid
        #This checks that no 2 numbers in the row are the same
        for iterate in sudoku:
                for number in iterate:
                        counter=iterate.count(number) 
                        if counter != 1:
                                validity=False 
                                #as soon as it becomes false the whole program disintergrates and becomes invalid
                                break 
                        
def colcheck(sudoku):     
        #This checks that no 2 numbers in the columns are the same
        sudcol1=[] #col 1 and col2 so that they can be discussed and iterated each 
        sudcol2=[]
        for number in sudoku:
                sudcol2.append(number)
        
                    
        for i in range(len(sudcol2)-1):
                for number in sudoku:
                        sudcol1.append(int(number[i]))
                                
        for i in range(9):
                for j in range(8):
                        if sudcol1[i]== sudcol2[j+1]:
                                validity=False
                                #as soon as it becomes false the whole program disintergrates and becomes invalid
                                break               


def the3x3grids(sudoku):
        #this function checks 3x3 grids for duplicates within the sudoku
        smallsud =[] #is an array with all three blocks in one list
        rownumber=0
        number='' #an empty list to add on when counter is greater than 0
        counter=9
        smallgrid1='' #the blocks refer ot the 3x3 smaller in the 9x9 sudoku grid
        smallgrid2=''
        smallgrid3=''
        while counter > 0:
                number = sudoku[rownumber]
                smallgrid1+=number[0:3]
                smallgrid2+=number[3:6]
                smallgrid3+=number[6:9]
                rownumber+=1
                counter-=3
                smallsud.append(smallgrid1)
                smallsud.append(smallgrid2)
                smallsud.append(smallgrid3)
                
        #this function checks 3x3 grids for duplicates within the sudoku
        rownumber=3
        number='' #an empty list to add on when counter is greater than 0
        counter=9
        smallgrid1='' #the blocks refer ot the 3x3 grids in the 9x9 array
        smallgrid2=''
        smallgrid3=''
        while counter > 0:
                number = sudoku[rownumber]
                smallgrid1+=number[0:3]
                smallgrid2+=number[3:6]
                smallgrid3+=number[6:9]
                rownumber+=1
                counter-=3
                smallsud.append(smallgrid1)
                smallsud.append(smallgrid2)
                smallsud.append(smallgrid3)
                       
        #this function checks 3x3 grids for duplicates within the sudoku
        rownumber=6
        number='' #an empty list to add on when counter is greater than 0
        counter=9
        smallgrid1='' #the blocks refer ot the 3x3 grids in the 9x9 array
        smallgrid2=''
        smallgrid3=''
        while counter > 0:
                number = sudoku[rownumber]
                smallgrid1+=number[0:3]
                smallgrid2+=number[3:6]
                smallgrid3+=number[6:9]
                rownumber+=1
                counter-=3
                smallsud.append(smallgrid1)
                smallsud.append(smallgrid2)
                smallsud.append(smallgrid3)                
                                
#check for any values that are the same in the 3x3 in the small grids
                                
        for iterate in smallsud:
                        for i in iterate:
                                valueamount = iterate.count(i)
                                if valueamount  > 1:
                                        validity= False
                                        break

rowcheck(sudoku)
colcheck(sudoku)
the3x3grids(sudoku)
#final for validity and prints whether sudoku is or isnt valid
if validity == True:
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")