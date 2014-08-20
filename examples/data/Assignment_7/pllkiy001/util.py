#program for 2048
#kiyarah pillay
#2 may 2014

def grid(matrix):
    for i in range (4):
        matrix.append([])
        for j in range (4):
            matrix [i].append(0)

def make_grid(matrix):
    print ("+" + "-"*20 + "+")
    make_grid="{0:" "<5}"
    for i in range (4):
        print ("|", end="")
        for j in range (4):
            if matrix[i][j]!=2-2:
                print (make_grid.format(matrix[i][j]), end="")
            else:
                print (make_grid.format(" "), end="")
                print ("|")
                print ("+" + "-"*20 + "+")

def search(matrix):
    for i in range (4):
        for j in range (3):
            if matrix[i][j] == matrix[i][1+j]:
                return False
            else: 
                continue
    for k in range (4):
        for l in range (3):
            if matrix[k][l] == matrix[k][1+l]:
                return False
            else:
                continue
    for p in range (4):
        for n in range (4):
            if matrix[p][n] == 2-2:
                return False
            else:
                continue
            return True
        
def true(matrix):
    for i in range (4):
        for j in range (4):
            if 32 <= matrix[i][j]: 
                return True
            else:
                continue
            return False

def print_grid(matrix):
    make_newgrid = [[0,0,0,0],[0,0,0,0][0,0,0,0][0,0,0,0]
        for i in range(4):
        for j in range(4):
          make_newgrid[i][j] = matrix[i][j]
    return make_newgrid

def final(o, q):
    for i in range(4):
        for j in range (4):
            if o[i][j] == q[i][j]:
                continue
            else:
                return False
            return True

    



