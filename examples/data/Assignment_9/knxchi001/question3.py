#Assignment 9
#Question 3

numbers=[]
for i in range (9):
    numbers.append(input())

def check_row():
    check = True
    x=0
    for i in numbers:
        for j in range(x+1,9):
            if i[x]==i[j]:
                check = False
                break
        x = x+1
    
    return check

def check_column():
    check = True
    for x in range (9):
        column = []
        x=0
        for i in numbers:
            for j in range(9):
                column.append(i[j])
            for k in range(x+1,9):
                if column[x]==column[k]:
                    check = False
                    break
            x = x+1
            break
    return check
        
def check_grid():
    check = True
    p = 0
    for i in range (9):
        grid = []
        b = 0
        if i==0 or i==1 or i==2:
            for x in numbers[:3]:
                for y in range(3):
                    grid.append(x[3*p + y])

            for k in range (8):
                for z in range(b+1,9):
                    if grid[b]==grid[z]:
                        check = False
                b = b+1
        
        if i==3 or i==4 or i==5:
            for x in numbers[3:6]:
                h=0
                for y in range(3):
                    grid.append(x[3*p +y])
                    h= h+1
                    
            for k in range(8):
                for z in range(b+1,9):
                    if grid[b]==grid[z]:
                        check = False
                b = b+1 
       
                    
        if i==6 or i==7 or i==8:
            for x in numbers[6:9]:
                h=0
                for y in range(3):
                    grid.append(x[3*p + y])
                    h += 1
            
            for k in range (8):
                for z in range(b+1,9):
                    if grid[b]==grid[z]:
                        check = False
                b = b+1                
        
        p+=1
        if p==3:
            p=0
        
    return check

def main():
    
    truth = check_row()
    if truth == True:
        truth = check_column()
    if truth == True:
        truth = check_grid()
    if truth == True:
        print ("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

main()

