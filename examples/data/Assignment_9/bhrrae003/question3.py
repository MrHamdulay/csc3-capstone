def sudoku(r): 
    
    l = len(r)  
    integ = 1
    while integ <= l:
        i = 0
        while i < l:
            rcount = 0
            ccount = 0
            z = 0
            while z < l:
                if r[i][z] == integ:
                    rcount += 1
                if r[z][i] == integ:
                    ccount = ccount + 1
                z += 1
            if rcount != 1 or ccount != 1:
                return print("Sudoku grid is not valid")
            i = i +1
        integ += 1
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


new = []


a_numbers = eval(input()) 
a_str = str(a_numbers)  
for char in a_str:  
    a.append(int(char)) 

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



new.append(a)
new.append(b)
new.append(c)
new.append(d)
new.append(e)
new.append(f)
new.append(g)
new.append(h)
new.append(i)

sudoku(new)

