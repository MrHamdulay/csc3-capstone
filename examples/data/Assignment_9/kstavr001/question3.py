#Assignment 9,Question 3
#Avreyna Kistensamy
#11 May 2014

tracker = 'win'    #To keep track of correct grid

#Creating the Sudoku 2D grid
counter = 0
line = []
Sudoku = []
while counter < 9:
        numbers = input("")
        for i in range(9):
                line.append(str(numbers)[i])
        Sudoku.append(line)
        line = []
        counter+=1


#Checking rows
for row in range(9):
        total = 0
        for i in Sudoku[row]:
                total += int(i)
        if total != 45:                 #Sum of 1 to 9 = 45
                tracker = 'lose'
                print("Sudoku grid is not valid")
                break
#total = 0       
#Checking columns
if tracker == 'win':
        for row in range(9):
                total = 0
                for col in range(9):
                        total += int(Sudoku[row][col])
                if total != 45:
                        tracker = 'lose'
                        print("Sudoku grid is not valid")
                        break 


#Checking the boxes
def box_check(a,b):
        global tracker
        total = 0
        for row in range(a,b):
                for col in range(3):
                        total += int(Sudoku[row][col])
        if total == 45:
                total = 0
                for row in range(a,b):
                        for col in range(3,6):
                                total += int(Sudoku[row][col]) 
        if total == 45:
                total = 0
                for row in range(a,b):
                        for col in range(6,9):
                                total += int(Sudoku[row][col])                
        if total != 45:
                tracker = 'lose' 
                print("Sudoku grid is not valid")
                
                 

#Only checking boxes while grid is still correct
if tracker == 'win':
        box_check(0,3)
        if tracker == 'win':
                box_check(3,6)
                if tracker == 'win':
                        box_check(6,9)        
                        if tracker == 'win':
                                print("Sudoku grid is valid")
                
                        
                        





