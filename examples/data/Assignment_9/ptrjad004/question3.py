"""A program to check if a complete Sudoku grid is valid or not
Jade Petersen
Assignment 9 
Question 3
15 May 2014"""


def check_sudoku(p): 
    
    z = len(p)    #finds length of the 2D array
    number = 1
    while number <= z:
        i = 0
        while i < z:
            row_count = 0
            col_count = 0
            j = 0
            while j < z:
                if p[i][j] == number:
                    row_count = row_count + 1
                if p[j][i] == number:
                    col_count = col_count + 1
                j = j+1
            if row_count != 1 or col_count != 1:
                return print("Sudoku grid is not valid")
            i = i +1
        number = number + 1
    return print("Sudoku grid is valid")

# = 9 seperate lists to store each sudoku grid
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

