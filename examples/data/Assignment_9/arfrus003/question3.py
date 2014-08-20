def sudoku(u): 
    
    l = len(u)  #finds length of the 2d array
    dig = 1
    while dig <= l:
        i = 0
        while i < l:
            rcount = 0
            ccount = 0
            z = 0
            while z < l:
                if u[i][z] == dig:
                    rcount += 1
                if u[z][i] == dig:
                    ccount = ccount + 1
                z += 1
            if rcount != 1 or ccount != 1:
                return print("Sudoku grid is not valid")
            i = i +1
        dig += 1
    return print("Sudoku grid is valid")


a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []


combo = []


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
combo.append(a)
combo.append(b)
combo.append(c)
combo.append(d)
combo.append(e)
combo.append(f)
combo.append(g)
combo.append(h)
combo.append(i)

sudoku(combo)

