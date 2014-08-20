"""check soduku
Sachin Murugan
15/5/2014"""
def sudoku_grid():
        sudlist = []
        for i in range(9):
                rowgrid = []
                row = input("")
                for j in range (len(row)):
                        rowgrid.append(row[j])
                
                sudlist.append(rowgrid)
        return sudlist 


def check_sudoku_row(sudlist):
        for rowz in range(0,9):
                temporary = sudlist[rowz]
                breaks ='no'
                rowz = 'good'
        
        for numb in temporary:
                Repeat = temporary.count(numb)
                if Repeat > 1:
                        breaks= "yes"
                        break
                if breaks == 'yes':
                        rowz = 'bad'
                        break
       
        return rowz
        
def check_sudoku_column(sudlist):# a repetitive check to check each column for no repeats
    
        column1 = [sudlist[0][0], sudlist[1][0], sudlist[2][0], sudlist[3][0], sudlist[4][0], sudlist[5][0], sudlist[6][0], sudlist[7][0], sudlist[8][0]]
        
        column2 = [sudlist[0][1], sudlist[1][1], sudlist[2][1], sudlist[3][1], sudlist[4][1], sudlist[5][1], sudlist[6][1], sudlist[7][1], sudlist[8][1]]

        column3 = [sudlist[0][2], sudlist[1][2], sudlist[2][2], sudlist[3][2], sudlist[4][2], sudlist[5][2], sudlist[6][2], sudlist[7][2], sudlist[8][2]]

        column4 = [sudlist[0][3], sudlist[1][3], sudlist[2][3], sudlist[3][3], sudlist[4][3], sudlist[5][3], sudlist[6][3], sudlist[7][3], sudlist[8][3]]

        column5 = [sudlist[0][4], sudlist[1][4], sudlist[2][4], sudlist[3][4], sudlist[4][4], sudlist[5][4], sudlist[6][4], sudlist[7][4], sudlist[8][4]]

        column6 = [sudlist[0][5], sudlist[1][5], sudlist[2][5], sudlist[3][5], sudlist[4][5], sudlist[5][5], sudlist[6][5], sudlist[7][5], sudlist[8][5]]

        column7 = [sudlist[0][6], sudlist[1][6], sudlist[2][6], sudlist[3][6], sudlist[4][6], sudlist[5][6], sudlist[6][6], sudlist[7][6], sudlist[8][6]]

        column8 = [sudlist[0][7], sudlist[1][7], sudlist[2][7], sudlist[3][7], sudlist[4][7], sudlist[5][7], sudlist[6][7], sudlist[7][7], sudlist[8][7]]

        column9 = [sudlist[0][8], sudlist[1][8], sudlist[2][8], sudlist[3][8], sudlist[4][8], sudlist[5][8], sudlist[6][8], sudlist[7][8], sudlist[8][8]]
    
        SudColumn = 'good'
        n = 0
    
        for i in column1:
                rep1 = column1.count(i)
                if rep1 > 1:
                        n=n+1
        for i in column2:
                rep2 = column2.count(i)
                if rep2 > 1:
                        n=n+1
        for i in column3:
                rep3 = column3.count(i)
                if rep3 > 1:
                        n=n+1
        for i in column4:
                rep4 = column4.count(i)
                if rep4 > 1:
                        n=n+1
        for i in column5:
                rep5 = column5.count(i)
                if rep5 > 1:
                        n=n+1
        for i in column6:
                rep6 = column6.count(i)
                if rep6 > 1:
                        n=n+1
        for i in column7:
                rep7 = column7.count(i)
                if rep7 > 1:
                        n=n+1
        for i in column8:
                rep8 = column8.count(i)
                if rep8 > 1:
                        n=n+1
        for i in column9:
                rep9 = column9.count(i)
                if rep9 > 1:
                        n=n+1
            
        if n > 1:
                SudColumn = 'bad'

        return SudColumn

def Checker(sudlist):
        x = []
        for row in sudlist:
                lines = row[0:3]
                x.append(lines)
        y = []
        for row in sudlist:
                lines = row[3:6]
                y.append(lines)
        
        z = []
        for row in sudlist:
                lines = row[6:]
                z.append(lines)
    
        checknumb1 = x[:3]
        checknumb2 = y[:3]
        checknumb3 = z[:3]
        checknumb4 = x[3:6]
        checknumb5 = y[3:6]
        checknumb6 = z[3:6]
        checknumb7 = x[6:]
        checknumb8 = y[6:]
        checknumb9 = z[6:]
    
        newlines = []
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb1[i][j]
        newlines.append(lines)
    
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb2[i][j]    
        newlines.append(lines)
        
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb3[i][j]    
        newlines.append(lines)
    
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb4[i][j]    
        newlines.append(lines)  
    
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb5[i][j]    
        newlines.append(lines) 
    
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb6[i][j]    
        newlines.append(lines)    
    
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb7[i][j]    
        newlines.append(lines)    
    
        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb8[i][j]    
        newlines.append(lines)    

        lines=""
        for i in range(3):
                for j in range(3):
                        lines += checknumb9[i][j]    
        newlines.append(lines)    
    
        Valid = True
        
        for lines in newlines:
                for i in lines:
                        rep = lines.count(i)
                        if rep > 1:
                                right = False
                                break 
    
        gsum1 = 0
        for row1 in checknumb1:
                Rsum1 = 0
                for numb1 in row1:
                        Rsum1 += eval(numb1)
                        gsum1+= Rsum1
        
        gsum2 = 0
        for row2 in checknumb2:
                Rsum2 = 0
                for numb2 in row2:
                        Rsum2 += eval(numb2)
                        gsum2+= Rsum2
        
        gsum3 = 0
        for row3 in checknumb3:
                Rsum3 = 0
                for numb3 in row3:
                        Rsum3 += eval(numb3)
                        gsum3+= Rsum3
                        
        gsum4 = 0
        for row4 in checknumb4:
                Rsum4 = 0
                for numb4 in row4:
                        Rsum4 += eval(numb4)
                        gsum4+= Rsum4
        
        gsum5 = 0
        for row5 in checknumb5:
                Rsum5 = 0
                for numb5 in row5:
                        Rsum5 += eval(numb5)
                        gsum5+= Rsum5
        
        gsum6 = 0
        for row6 in checknumb6:
                Rsum6 = 0
                for numb6 in row6:
                        Rsum6 += eval(numb6)
                        gsum6+= Rsum6
    
        gsum7= 0
        for row7 in checknumb7:
                Rsum7 = 0
                for numb7 in row7:
                        Rsum7 += eval(numb7)
                        gsum7+= Rsum7
        
        gsum8 = 0
        for row8 in checknumb8:
                Rsum8 = 0
                for numb8 in row8:
                        Rsum8 += eval(numb8)
                        gsum8+= Rsum8
        
        gsum9 = 0
        for row9 in checknumb9:
                Rsum9 = 0
                for numb9 in row9:
                        Rsum9 += eval(numb9)
                        gsum9+= Rsum9
    
        Tsum = gsum1 + gsum2 + gsum3 + gsum4 + gsum5 + gsum6 + gsum7 + gsum8 + gsum9
    
        return Tsum,right
                
def main():
        sudlist = sudoku_grid()

        validA = check_sudoku_row(sudlist)
        
        validB = check_sudoku_column(sudlist)
    
        validC,right = Checker(sudlist)
    
        if validA == 'good' and validB == 'good' and validC == 405 and right == True:
                print("Sudoku grid is valid")
        
        else:
                print("Sudoku grid is not valid")
main()