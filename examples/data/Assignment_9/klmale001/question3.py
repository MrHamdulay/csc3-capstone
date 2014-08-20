"""Question 3
15 May 2014
Alexi Kalamoudacos"""

def CheckRows(l):
    #scanning the rows in the table
    x=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] in x: #extracting the data to compare later
                return False      #
            else:
                x.append(l[i][j])
        x=[]
    return True
def CheckCollumns(l):
    #scanning the columns in the table
    c=[]
    for i in range(9):
        for j in range(9):
            if l[j][i] in c:
                return False
            else:
                c.append(l[j][i])
        c=[]
    return True
def CheckGrid(l):
    #scanning the smaller tables in the table
    d=0
    y=0
    for SudokuLine1 in range(3):
        g=[]
        for i in range(d,d+3):
            #scan entire table
            for j in range(y,y+3):
                if l[i][j] in g:
                    return False
                else:
                    g.append(l[i][j])
          
          
        d+=3
        g=[]
    y=3
    d=0
    for SudokuLine2 in range(3):
        g=[]
        for i in range(d,d+3):
            for j in range(y,y+3):
                if l[i][j] in g:
                    return False
                else:    
                    g.append(l[i][j])                
        d+=3
        g=[]
      
    d=0    
    y=6
    for SudokuLine3 in range(3):
        g=[]
        for i in range(d,d+3):
            for j in range(y,+3):
                if l[i][j] in g:
                    return False
                else:    
                    g.append(l[i][j])                
        d+=3
        g=[]        
    return True
          
w=[]        
for i in range(9):
    #requesting input
    q=input('')
    w.append(q)
if (CheckRows(w)) and (CheckCollumns(w)) and CheckGrid(w):
    print('Sudoku grid is valid')
else:
    print('Sudoku grid is not valid')