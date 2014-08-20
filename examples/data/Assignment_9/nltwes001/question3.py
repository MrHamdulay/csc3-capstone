#ASSIGNMENT 9
#QUESTION 3
#NLTWES001

grid=[]
for i in range (9):
    grid.append(input())

def rowcheck():
    valid = True
    pos=0
    for i in grid:
        for j in range(pos+1,9):
            if i[j]==i[i]:
                valid = False
                break
        pos+=1
    return valid

def columncheck():
    valid = True
    for pos in range(9):
        column=[]
        pos=0
        for y in grid:
            for w in range(9):
                column.append(y[w])
            
            for z in range(pos+1,9):
                if column[pos]==column[z]:
                    valid = False
                    break
            pos = pos+1
            break
    return valid 
        
def gridcheck():
    valid = True
    p=0
    for i in range (9):
        grid=[]
        b=0
        if i==0 or i==1 or i==2:
            for pos in grid[:3]:
                for y in range(3):
                    grid.append(pos[3*p + y])

            for k in range (8):
                for z in range(b+1,9):
                    if grid[b]==grid[z]:
                        valid = False
                b = b+1
        
        if i==3 or i==4 or i==5:
            for pos in grid[3:6]:
                h=0
                for y in range(3):
                    grid.append(pos[3*p +y])
                    h= h+1
                    
            for k in range(8):
                for z in range(b+1,9):
                    if grid[b]==grid[z]:
                        valid = False
                b = b+1 
                    
        if i==6 or i==7 or i==8:
            for pos in grid[6:9]:
                h=0
                for y in range(3):
                    grid.append(pos[3*p + y])
                    h += 1
            
            for k in range (8):
                for z in range(b+1,9):
                    if grid[b]==grid[z]:
                        valid = False
                b = b+1                
        p+=1
        if p==3:
            p=0
    return valid

def main():
    truth = rowcheck()
    if truth == True:
        truth = columncheck()
    if truth == True:
        truth = gridcheck()
    if truth == True:
        print ("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

main()