#A program to check whether a suduko grid is valid
#Created by: Jenna Lake
#Date:16 may 2014


#get input line by line, appending each line to list1
list1=[]
for i in range(9):
    put_in=input()
    list1.append(put_in)

#append each number separately
list2=[]
list3=[]
for row in range(9):
    for col in range(9):
        list2.append(list1[row][col])
    list3.append(list2)
    list2=[]

game_win=True
#check if each row is correct, if any row has a repeated number, game_win becomes false and columns and 3 by 3 grid not tested
for row in range(9):
    for col in range(9):
        x=list3[row][col]
        for i in range(9):
            if i!=col:
                if x==list3[row][i]:
                    game_win=False
#check if each column is correct
if game_win==True:
    for x in range (9):
            column = []
            x=0
            for y in list3:
                for w in range(9):
                    column.append(y[w])
                
                for z in range(x+1,9):
                    if column[x]==column[z]:
                        valid = False
                        break
                x = x+1
                break
                              
#check if each 3 by 3 block is correct
if game_win==True:      #only checks if grid is correct if game_win is not already false(only need one to prove grids invalid)
    
    listblock=[]
    str1=""
    for row in range(3):
        block_row=3*row
        for col in range(3):
            block_col=3*col
            for i in range(3):
                for j in range(3):
                    str1+=list3[i+block_row][j+block_col]
            listblock.append(str1)      #first make a list of values ordered such that the 9 numbers are the lines in the 3 by 3 block
            str1=""
    
    for row in range(9):
        for col in range(9):
            x=listblock[row][col]
            for i in range(9):
                if i!=col:
                    if x==listblock[row][i]:
                        game_win=False
                        break
if game_win==False:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")
