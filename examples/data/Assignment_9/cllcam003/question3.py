# Cameron Collum 
# Checks validity of sudoku puzzle
# 17/05/2014

import collections

sudoku_grid=[[],[],[],[],[],[],[],[],[]]

sudoku_grid[0]=input()
sudoku_grid[1]=input()
sudoku_grid[2]=input()
sudoku_grid[3]=input()
sudoku_grid[4]=input()
sudoku_grid[5]=input()
sudoku_grid[6]=input()
sudoku_grid[7]=input()
sudoku_grid[8]=input()


# analyse rows for copies
repeat_row=[]
answer_row=[]
for row in sudoku_grid: 
    count_row=collections.Counter(row)
    for x in count_row:
        if count_row[x]>1:
            answer_row.append(1) 
            break
        else:
            continue

answer_col=[] 

            
if 1 in answer_row:
    ()

# checks columns    
else:
    col_count = [[],[],[],[],[],[],[],[],[]]
    for row in sudoku_grid:
        count=0
        for col in row:
            col_count[count].append(col)
            count+=1
            
            
    for row1 in sudoku_grid:
        col_count=collections.Counter(row1)
        for y in col_count:
            if col_count[y]>1:
                answer_col.append(1) 
                break
            else:
                continue


#if there is a 1 in answer_col its invalid
if 1 in answer_col:
    ()

else:
    blocks = [[],[],[],[],[],[],[],[],[]]  
    row_step = 0  
    pos = 0 
    end_of_grid = 0 #makes sure index within range
    for row in sudoku_grid: #looks at each row 
        step = 0  
        if row_step<3: 
            if end_of_grid<3:
                pos=0  
            elif 2<end_of_grid<6: 
                pos=3 
            elif 5<end_of_grid<9:
                pos=6 
            
        else: 
            if end_of_grid==3: 
                pos = 3 
                row_step = 0 
            elif end_of_grid==6: 
                pos = 6  
                row_step = 0 
            else:
                ()
        row_step += 1 # new row 
        end_of_grid +=1 
        for place in row: # looks at the values in the row 
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
            answer_blocks.append(1)  
            break
        else:
            continue
        
if 1 in answer_blocks or 1 in answer_row or 1 in answer_col:
    print("Sudoku grid is not valid")

else:
    print("Sudoku grid is valid")
            
            
            
            
            
           
