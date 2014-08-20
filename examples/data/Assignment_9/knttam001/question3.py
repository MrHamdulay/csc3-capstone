"""program to test if a sudoku grid is valid
Tamsin Kantor
May 2014"""

# initilizing horizontal lists
line1 = input()
h1 = list(line1)
line2 = input()
h2 = list(line2)
line3 = input()
h3 = list(line3)
line4 = input()
h4 = list(line4)
line5 = input()
h5 = list(line5)
line6 = input()
h6 = list(line6)
line7 = input()
h7 = list(line7)
line8 = input()
h8 = list(line8)
line9 = input()
h9 = list(line9)

#initializing vertical lists
v1 = [h1[0],h2[0],h3[0],h4[0],h5[0],h6[0],h7[0],h8[0],h9[0]]
v2 = [h1[1],h2[1],h3[1],h4[1],h5[1],h6[1],h7[1],h8[1],h9[1]]
v3 = [h1[2],h2[2],h3[2],h4[2],h5[2],h6[2],h7[2],h8[2],h9[2]]
v4 = [h1[3],h2[3],h3[3],h4[3],h5[3],h6[3],h7[3],h8[3],h9[3]]
v5 = [h1[4],h2[4],h3[4],h4[4],h5[4],h6[4],h7[4],h8[4],h9[4]]
v6 = [h1[5],h2[5],h3[5],h4[5],h5[5],h6[5],h7[5],h8[5],h9[5]]
v7 = [h1[6],h2[6],h3[6],h4[6],h5[6],h6[6],h7[6],h8[6],h9[6]]
v8 = [h1[7],h2[7],h3[7],h4[7],h5[7],h6[7],h7[7],h8[7],h9[7]]
v9 = [h1[8],h2[8],h3[8],h4[8],h5[8],h6[8],h7[8],h8[8],h9[8]]

# initilizing grid lists
g1 = [h1[0],h1[1],h1[2],h2[0],h2[1],h2[2],h3[0],h3[1],h3[2]]
g2 = [h1[3],h1[4],h1[5],h2[3],h2[4],h2[5],h3[3],h3[4],h3[5]]
g3 = [h1[6],h1[7],h1[8],h2[6],h2[7],h2[8],h3[6],h3[7],h3[8]]
g4 = [h4[0],h4[1],h4[2],h5[0],h5[1],h5[2],h6[0],h6[1],h6[2]]
g5 = [h4[3],h4[4],h4[5],h5[3],h5[4],h5[5],h6[3],h6[4],h6[5]]
g6 = [h4[6],h4[7],h4[8],h5[6],h5[7],h5[8],h6[6],h6[7],h6[8]]
g7 = [h7[0],h7[1],h7[2],h8[0],h8[1],h8[2],h9[0],h9[1],h9[2]]
g8 = [h7[3],h7[4],h7[5],h8[3],h8[4],h8[5],h9[3],h9[4],h9[5]]
g9 = [h7[6],h7[7],h7[8],h8[6],h8[7],h8[8],h9[6],h9[7],h9[8]]

# combining the lists
numbers = ["1","2","3","4","5","6","7","8","9"]
horizontal = [h1,h2,h3,h4,h5,h6,h7,h8]
vertical = [v1,v2,v3,v4,v5,v6,v7,v8,v9]
grids = [g1,g2,g3,g4,g5,g6,g7,g8,g9]

tester = 0

# checking horziontally
for x in horizontal:
        for n in numbers:
                if x.count(n) != 1:
                        tester += 1
# checking vertically
for x in vertical:
        for n in numbers:
                if x.count(n) != 1:
                        tester += 1

#checking grids
for x in grids:
        for n in numbers:
                if x.count(n) != 1:
                        tester += 1

# final test
if tester == 0:
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")