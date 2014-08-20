'''Program to check if a sudoku grid is valid
By Daniel Newton
10/05/14'''

sudokugrid=[]
for i in range(9):      #creates 9x9 empty grid
    sudokugrid.append([0]*9)

#asks for 9 rows on input
a=input()
b=input()
c=input()
d=input()
e=input()
f=input()
g=input()
h=input()
i=input()

#fills grid with numbers supplied
for num in range(9):
    sudokugrid[0][num]=a[num]
    sudokugrid[1][num]=b[num]
    sudokugrid[2][num]=c[num]
    sudokugrid[3][num]=d[num]
    sudokugrid[4][num]=e[num]
    sudokugrid[5][num]=f[num]
    sudokugrid[6][num]=g[num]
    sudokugrid[7][num]=h[num]
    sudokugrid[8][num]=i[num]

def row_col_check():    #checks if any numbers in corresponding rows or columns are equal
    for f in range(9):
        for i in range(9):
            for j in range(9):
                if i==j:
                    continue
                elif sudokugrid[f][i]==sudokugrid[f][j] or sudokugrid[j][f]==sudokugrid[i][f]:
                    return False
    return True

def boxcheck():     #Checks if numbers in 3 x 3 boxes are equal
    box=[]
    for i in range(0,7,3):
        for j in range(0,7,3):
            for f in range(3):
                for g in range(3):
                    box.append(sudokugrid[i+f][j+g])
            if len(set(box))<9:
                return False
            box=[]
        
    
#Evaluates whether grid is overall valid as a soduku grid or not
if row_col_check()==False or boxcheck()==False:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")