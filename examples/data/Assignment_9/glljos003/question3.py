"""program to check if a complete sudoku grid is valid or not
joshua gullan
11 may 2014"""

import collections

grid_array=[[],[],[],[],[],[],[],[],[]]

grid_array[0]=input()
grid_array[1]=input()
grid_array[2]=input()
grid_array[3]=input()
grid_array[4]=input()
grid_array[5]=input()
grid_array[6]=input()
grid_array[7]=input()
grid_array[8]=input()


#checks for duplicates in row
duplicate_row=[]
answer_row=[]
for row in grid_array: 
    count_row=collections.Counter(row)
    for x in count_row:
        if count_row[x]>1:
            answer_row.append(1)  #if there is a duplicate, append 1 to answer_row
            break
        else:
            continue

answer_col=[] #used later

#if there is a 1 in answer_row, there is a duplicate and the grid is invalid            
if 1 in answer_row:
    ()

#if there is no 1, the grid rows are valid, now checks columns    
else:
    count_col = [[],[],[],[],[],[],[],[],[]]
    for row in grid_array:
        count=0
        for col in row:
            count_col[count].append(col)
            count+=1
            
            
    for row1 in grid_array:
        count_col=collections.Counter(row1)
        for y in count_col:
            if count_col[y]>1:
                answer_col.append(1) #if there is a duplicate, append 1 to answer_col
                break
            else:
                continue


#if there is a 1 in answer_col, there is a duplicate and the grid is invalid
if 1 in answer_col:
    ()

else:
    blocks = [[],[],[],[],[],[],[],[],[]]  #new 3 by 3 grids
    row_step = 0  #y position within new grid
    pos = 0 #new grid index
    end_of_grid = 0 #used to ensure index within range
    for row in grid_array: #looking at each horizontal row within the main grid
        step = 0  #x position of the values IN the row of the main grid
        if row_step<3: #if y is under 3, check which grids we're looking at
            if end_of_grid<3:
                pos=0 #looking at grids 0,1,2 so the values must be appended starting at position 0 and going to 2 
            elif 2<end_of_grid<6: 
                pos=3 #looking at grids 3,4,5 so the values must be appended starting at position 3 and going to 5
            elif 5<end_of_grid<9:
                pos=6 #looking at grids 6,7,8 so the values must be appended starting at position 6 and going to 8
            
        else: #if y is 3, we are dealing with a new line in the new grids
            if end_of_grid==3: #if we're on the 4th line, the grid is 3
                pos = 3 #looking at grids 3,4,5
                row_step = 0 #set back to 0 so we can populate first line of grid 3
            elif end_of_grid==6: #if we're on the 6th line, the grid is 6
                pos = 6 #looking at grids 6,7,8 
                row_step = 0 #set back to 0 so we can populate first line of grid 6
            else:
                ()
        row_step += 1 #we're on a new row in the main grid after the following loops, so we must count it now
        end_of_grid +=1 
        for place in row: #this loop looks at the values IN the row iterated by the outer loop and appends values to corresponding grid.
            if step==0 or step==1 or step==2:
                if end_of_grid==1 or end_of_grid==2 or end_of_grid==3:
                    blocks[0].append(place)
                    
                elif end_of_grid==4 or end_of_grid==5 or end_of_grid==6:
                    blocks[3].append(place)                
                
                elif end_of_grid==7 or end_of_grid==8 or end_of_grid==9:
                    blocks[6].append(place)
            
            elif step==3 or step==4 or step==5:
                if end_of_grid==1 or end_of_grid==2 or end_of_grid==3:
                    blocks[1].append(place)
                                       
                elif end_of_grid==4 or end_of_grid==5 or end_of_grid==6:
                    blocks[4].append(place)                
                                   
                elif end_of_grid==7 or end_of_grid==8 or end_of_grid==9:
                    blocks[7].append(place)
            
            elif step==6 or step==7 or step==8:
                if end_of_grid==1 or end_of_grid==2 or end_of_grid==3:
                    blocks[2].append(place)
                    
                elif end_of_grid==4 or end_of_grid==5 or end_of_grid==6:
                    blocks[5].append(place)                
                
                elif end_of_grid==7 or end_of_grid==8 or end_of_grid==9:
                    blocks[8].append(place)            
            step+=1
            
 
duplicate_blocks=[]
answer_blocks=[]
for row in blocks: 
    count_blocks=collections.Counter(row)
    for x in count_blocks:
        if count_blocks[x]>1:
            answer_blocks.append(1)  #if there is a duplicate, append 1 to answer_row
            break
        else:
            continue
        
if 1 in answer_blocks or 1 in answer_row or 1 in answer_col:
    print("Sudoku grid is not valid")

else:
    print("Sudoku grid is valid")
            
            
            
            
            
           
