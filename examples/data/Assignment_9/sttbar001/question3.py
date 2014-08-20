"""check if a complete Sudoku grid is valid or not.
barak setton
11/05/2014"""


"""
259716483
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861
"""

#array = [] # making the 3X3 array of 3X3 arrays
info =input()
for a in range(8):
    info = info + input()
array =[[list(info[0:3]), list(info[9:12]), list(info[18:21])], [list(info[3:6]), list(info[12:15]), list(info[21:24])], [list(info[6:9]), list(info[15:18]), list(info[24:27])]], [[list(info[27:30]), list(info[36:39]), list(info[45:48])],[list(info[30:33]), list(info[39:42]), list(info[48:51])],[list(info[33:36]), list(info[42:45]), list(info[51:54])]], [[list(info[54:57]), list(info[63:66]), list(info[72:75])], [list(info[57:60]), list(info[66:69]), list(info[75:78])], [list(info[60:63]), list(info[69:72]), list(info[78:81])]]
# making the array

v =0
# check blocks to make sure they are fine
tot =0
for blockr in range (3):
    for blockc in range(3):
        for row in range(3):
            for col in range(3):
                tot = tot + eval(array[blockr][blockc][row][col])
        if tot != 45:
            v =1
        tot=0

# checking rows
tot =0
for blockr in range (3):
    for row in range(3):
        for blockc in range(3):
            for col in range(3):
                tot = tot + eval(array[blockr][blockc][row][col])
                
        if tot != 45:
            v=1
        tot=0  
# checks the colombs
tot =0
for blockc in range (3):
    for col in range(3):
        for blockr in range(3):
            for row in range(3):
                tot = tot + eval(array[blockr][blockc][row][col])
               

        if tot != 45:
            v=1
        tot=0
        
if v==1:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
