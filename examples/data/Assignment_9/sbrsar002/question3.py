# 15 May 2014
# Sarayn Subroyen
# A program to check if a complete Sudoku grid is valid or not


def check_sudoku(p): 
    
    s = len(p)                                       #finds length of the 2d array
    num = 1
    while num <= s:
        i = 0
        while i < s:
            row = 0
            col = 0
            j = 0
            while j < s:
                if p[i][j] == num:
                    row = row + 1
                if p[j][i] == num:
                    col = col + 1
                j = j+1
            if row != 1 or col!= 1:
                return print("Sudoku grid is not valid")
            i = i +1
        num = num + 1
    return print("Sudoku grid is valid")

# lists to store each sudoku grid
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
merge = []


a_numbers = eval(input())                          #enter each grid
a_str = str(a_numbers)                             #converts the numbers to integers
for ch in a_str:  
    a.append(int(ch))                              #appends the numbers into their respective grids

b_numbers = eval(input())
b_str = str(b_numbers)
for ch in b_str:
    b.append(int(ch))
    
c_numbers = eval(input())
c_str = str(c_numbers)
for ch in c_str:
    c.append(int(ch))

d_numbers = eval(input())
d_str = str(d_numbers)
for ch in d_str:
    d.append(int(ch))
    
e_numbers = eval(input())
e_str = str(e_numbers)
for ch in e_str:
    e.append(int(ch))

f_numbers = eval(input())
f_str = str(f_numbers)
for ch in f_str:
    f.append(int(ch))

g_numbers = eval(input())
g_str = str(g_numbers)
for ch in g_str:
    g.append(int(ch))

h_numbers = eval(input())
h_str = str(h_numbers)
for ch in h_str:
    h.append(int(ch))

i_numbers = eval(input())
i_str = str(i_numbers)
for ch in i_str:
    i.append(int(ch))


#appends each inputed grid into one 2D array
merge.append(a)
merge.append(b)
merge.append(c)
merge.append(d)
merge.append(e)
merge.append(f)
merge.append(g)
merge.append(h)
merge.append(i)

check_sudoku(merge)

