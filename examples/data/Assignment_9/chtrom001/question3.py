# question3.py
# A program to check if a complete Sudoku grid is valid or not. 
# romelon43435
# 10 may 2014


def Getgrid():
    # This function is used to get the input Soduku grid and create a list from it
    Grid = []
    for i in range(9):
        r = []
        row = input("")
        for j in range (len(row)):
            r.append(row[j])
        #row.split(' ')
        Grid.append(r)
    #print(Grid)
    
    return Grid


def checkrow(Grid):
    # This function checks all the rows by iterating through it and checking for repetition of any numbers
    for rows in range(0,9):
        tempR = Grid[rows]
        brk = 'no'
        rows = 'good'
        for number in tempR:
            rep = tempR.count(number)
            if rep > 1:
                brk = "yes"
                break
        if brk == 'yes':
            rows = 'bad'
            #print("Sudoku grid is not valid")
            break
       
        return rows
        
def checkcol(Grid):
    #This function is used to check a column for repetition of numbers
    col1 = [Grid[0][0], Grid[1][0], Grid[2][0], Grid[3][0], Grid[4][0], Grid[5][0], Grid[6][0], Grid[7][0], Grid[8][0]]
    #print("here is col1: ",col1)
    col2 = [Grid[0][1], Grid[1][1], Grid[2][1], Grid[3][1], Grid[4][1], Grid[5][1], Grid[6][1], Grid[7][1], Grid[8][1]]
    #print("here is col2: ",col2)
    col3 = [Grid[0][2], Grid[1][2], Grid[2][2], Grid[3][2], Grid[4][2], Grid[5][2], Grid[6][2], Grid[7][2], Grid[8][2]]
    #print("here is col3: ",col3)
    col4 = [Grid[0][3], Grid[1][3], Grid[2][3], Grid[3][3], Grid[4][3], Grid[5][3], Grid[6][3], Grid[7][3], Grid[8][3]]
    #print("here is col4: ",col4)
    col5 = [Grid[0][4], Grid[1][4], Grid[2][4], Grid[3][4], Grid[4][4], Grid[5][4], Grid[6][4], Grid[7][4], Grid[8][4]]
    #print("here is col5: ",col5)
    col6 = [Grid[0][5], Grid[1][5], Grid[2][5], Grid[3][5], Grid[4][5], Grid[5][5], Grid[6][5], Grid[7][5], Grid[8][5]]
    #print("here is col6: ",col6)
    col7 = [Grid[0][6], Grid[1][6], Grid[2][6], Grid[3][6], Grid[4][6], Grid[5][6], Grid[6][6], Grid[7][6], Grid[8][6]]
    #print("here is col7: ",col7)
    col8 = [Grid[0][7], Grid[1][7], Grid[2][7], Grid[3][7], Grid[4][7], Grid[5][7], Grid[6][7], Grid[7][7], Grid[8][7]]
    #print("here is col1: ",col8)
    col9 = [Grid[0][8], Grid[1][8], Grid[2][8], Grid[3][8], Grid[4][8], Grid[5][8], Grid[6][8], Grid[7][8], Grid[8][8]]
    #print("here is col9: ",col9)
    
    cols = 'good'
    x = 0
    
    for a in col1:
            repa = col1.count(a)
            if repa > 1:
                x=x+1
    for b in col2:
            repb = col2.count(b)
            if repb > 1:
                x=x+1
    for c in col3:
            repc = col3.count(c)
            if repc > 1:
                x=x+1
    for d in col4:
            repd = col4.count(d)
            if repd > 1:
                x=x+1
    for e in col5:
            repe = col5.count(d)
            if repe > 1:
                x=x+1
    for f in col6:
            repf = col6.count(e)
            if repf > 1:
                x=x+1
    for g in col7:
            repg = col7.count(g)
            if repg > 1:
                x=x+1
    for h in col8:
            reph = col8.count(h)
            if reph > 1:
                x=x+1
    for i in col9:
            repi = col9.count(i)
            if repi > 1:
                x=x+1
            
    if x > 1:
        cols = 'bad'

    return cols

def miniGridchecker(Grid):
    B = []
    for row in Grid:
        line = row[0:3]
        B.append(line)
        
    C = []
    for row in Grid:
        line = row[3:6]
        C.append(line)
        
    D = []
    for row in Grid:
        line = row[6:]
        D.append(line)
    
    grid1 = B[:3]
    grid2 = C[:3]
    grid3 = D[:3]
    grid4 = B[3:6]
    grid5 = C[3:6]
    grid6 = D[3:6]
    grid7 = B[6:]
    grid8 = C[6:]
    grid9 = D[6:]
    
    lines = []
    line=""
    for i in range(3):
        for j in range(3):
            line += grid1[i][j]
    lines.append(line)
    
    line=""
    for i in range(3):
        for j in range(3):
            line += grid2[i][j]    
    lines.append(line)
        
    line=""
    for i in range(3):
        for j in range(3):
            line += grid3[i][j]    
    lines.append(line)
    
    line=""
    for i in range(3):
        for j in range(3):
            line += grid4[i][j]    
    lines.append(line)  
    
    line=""
    for i in range(3):
        for j in range(3):
            line += grid5[i][j]    
    lines.append(line) 
    
    line=""
    for i in range(3):
        for j in range(3):
            line += grid6[i][j]    
    lines.append(line)    
    
    line=""
    for i in range(3):
        for j in range(3):
            line += grid7[i][j]    
    lines.append(line)    
    
    line=""
    for i in range(3):
        for j in range(3):
            line += grid8[i][j]    
    lines.append(line)    

    line=""
    for i in range(3):
        for j in range(3):
            line += grid9[i][j]    
    lines.append(line)    
    
    correct = True
    
    for line in lines:
        for number in line:
            rep = line.count(number)
            if rep > 1:
                correct = False
                break 
               
    #print(grid1)
    #print(grid2)
    #print(grid3)
    #print(grid4)
    #print(grid5)
    #print(grid6)
    #print(grid7)
    #print(grid8)
    #print(grid9)
    
    gsum1 = 0
    for row1 in grid1:
        Rsum1 = 0
        for numb1 in row1:
            Rsum1 += eval(numb1)
        gsum1+= Rsum1
        
    gsum2 = 0
    for row2 in grid2:
        Rsum2 = 0
        for numb2 in row2:
            Rsum2 += eval(numb2)
        gsum2+= Rsum2
        
    gsum3 = 0
    for row3 in grid3:
        Rsum3 = 0
        for numb3 in row3:
            Rsum3 += eval(numb3)
        gsum3+= Rsum3
        
    gsum4 = 0
    for row4 in grid4:
        Rsum4 = 0
        for numb4 in row4:
            Rsum4 += eval(numb4)
        gsum4+= Rsum4
        
    gsum5 = 0
    for row5 in grid5:
        Rsum5 = 0
        for numb5 in row5:
            Rsum5 += eval(numb5)
        gsum5+= Rsum5
        
    gsum6 = 0
    for row6 in grid6:
        Rsum6 = 0
        for numb6 in row6:
            Rsum6 += eval(numb6)
        gsum6+= Rsum6
    
    gsum7= 0
    for row7 in grid7:
        Rsum7 = 0
        for numb7 in row7:
            Rsum7 += eval(numb7)
        gsum7+= Rsum7
        
    gsum8 = 0
    for row8 in grid8:
        Rsum8 = 0
        for numb8 in row8:
            Rsum8 += eval(numb8)
        gsum8+= Rsum8
        
    gsum9 = 0
    for row9 in grid9:
        Rsum9 = 0
        for numb9 in row9:
            Rsum9 += eval(numb9)
        gsum9+= Rsum9
    
    Tsum = gsum1 + gsum2 + gsum3 + gsum4 + gsum5 + gsum6 + gsum7 + gsum8 + gsum9
    
    return Tsum,correct
                
def main():
    Grid = Getgrid()
    
    validR = checkrow(Grid)
    #print(validR)
    
    validC = checkcol(Grid)
    #print(validC)
    
    valid3,correct = miniGridchecker(Grid)
    #print(valid3)
    if validR == 'good' and validC == 'good' and valid3 == 405 and correct == True:
        print("Sudoku grid is valid")
        
    else:
        print("Sudoku grid is not valid")

main()