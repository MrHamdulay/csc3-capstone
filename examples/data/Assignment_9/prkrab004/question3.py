#Assignment 3
#Question 3
#Rabia Parker
#Due Date: 16/05/14

def sudoku(q): 
    
    length= len(q)  
    number = 1
    while number <= length:
        w = 0
        while w < length:
            cnt1 = 0
            cnt2 = 0
            cnt3 = 0
            while cnt3 < length:
                if q[w][cnt3] == number:
                    cnt1 += 1
                if q[cnt3][w] == number:
                    cnt2 = cnt2 + 1
                cnt3 += 1
            if cnt1 != 1 or cnt2 != 1:
                return print("Sudoku grid is not valid")
            w = w +1
        number += 1
    return print("Sudoku grid is valid")


r = []
a = []
b = []
i = []
p = []
k = []
e = []
h = []
w = []


List = []


rnum = eval(input()) 
r_word = str(rnum)  
for char in r_word:  
    r.append(int(char)) 

anum = eval(input())
a_word = str(anum)
for char in a_word:
    a.append(int(char))
    
bnum = eval(input())
b_word = str(bnum)
for char in b_word:
    b.append(int(char))

inum = eval(input())
i_word = str(inum)
for char in i_word:
    i.append(int(char))
    
pnum = eval(input())
p_word = str(pnum)
for char in p_word:
    p.append(int(char))

knum = eval(input())
k_word = str(knum)
for char in k_word:
    k.append(int(char))

enum = eval(input())
e_word = str(enum)
for char in e_word:
    e.append(int(char))

hnum = eval(input())
h_word = str(hnum)
for char in h_word:
    h.append(int(char))

wnum = eval(input())
w_word = str(wnum)
for char in w_word:
    w.append(int(char))



List.append(r)
List.append(a)
List.append(b)
List.append(i)
List.append(p)
List.append(k)
List.append(e)
List.append(h)
List.append(w)

sudoku(List)

