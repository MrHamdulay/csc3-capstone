"""Program to check validity of a complete soduku puzzle
tayla george
16 may 2014"""

def check_sudoku(solution): 
    number = len(solution)                               #finding the length of the array
    digit = 1
    while digit <= number:
        i = 0
        while i < number:
            rowcounter = 0
            colcounter = 0
            j = 0
            while j < number:
                if solution[i][j] == digit:
                    rowcounter+= 1
                if solution[j][i] == digit:
                    colcounter += 1
                j +=1
            if rowcounter != 1 or colcounter != 1:
                return print("Sudoku grid is not valid")
            i +=1
        digit += 1
    return print("Sudoku grid is valid")

# = Each 3x3 block of the completed soduku stored as an array
a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []

#the 9 grids in a single 2d-array
soduku = []


a_numbers = eval(input()) #entering each grid
a_str = str(a_numbers)  #converts the numbers to integers
for char in a_str:  
    a.append(int(char)) #appends the numbers into their respective grids

b_numbers = eval(input())
b_str = str(b_numbers)
for char in b_str:
    b.append(int(char))
    
c_numbers = eval(input())
c_str = str(c_numbers)
for char in c_str:
    c.append(int(char))

d_numbers = eval(input())
d_str = str(d_numbers)
for char in d_str:
    d.append(int(char))
    
e_numbers = eval(input())
e_str = str(e_numbers)
for char in e_str:
    e.append(int(char))

f_numbers = eval(input())
f_str = str(f_numbers)
for char in f_str:
    f.append(int(char))

g_numbers = eval(input())
g_str = str(g_numbers)
for char in g_str:
    g.append(int(char))

h_numbers = eval(input())
h_str = str(h_numbers)
for char in h_str:
    h.append(int(char))

i_numbers = eval(input())
i_str = str(i_numbers)
for char in i_str:
    i.append(int(char))


#appends each inputed grid into one 2D array
soduku.append(a)
soduku.append(b)
soduku.append(c)
soduku.append(d)
soduku.append(e)
soduku.append(f)
soduku.append(g)
soduku.append(h)
soduku.append(i)

check_sudoku(soduku)

