numbers=[]
for i in range (9):
    numbers.append(input())
#infile = open(input(),"r")
#for line in infile :
    #numbers.append(line)

def rowcheck():
    valid = True
    x=0
    for i in numbers:
    
        for y in range(x+1,9):
        
            if i[x]==i[y]:
                valid = False
                break
        x = x+1
    
    return valid

def columncheck():
    valid = True
    for x in range (9):
        column = []
        x=0
        for y in numbers:
            for w in range(9):
                column.append(y[w])
            
            for z in range(x+1,9):
                if column[x]==column[z]:
                    valid = False
                    break
            x = x+1
            break
    return valid 
        
def gridcheck():
    valid = True
    
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
                        valid = False
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
                        valid = False
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