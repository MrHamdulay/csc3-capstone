"""File line length modifier
Christoher Sterley
11/05/2014"""

soduku_file=[]

for grid_position in range(0,9):
    soduku_file.append(input())      

real_soduku=True #the grid is a real soduku grid until proven otherwise


for vertical in range(9):
    horizontal_check=[]
    for horizontal in range(9):
        if soduku_file[vertical][horizontal] in horizontal_check: #if the number is in the list, there is more than one of that number in the line
            real_soduku=False
        else:
            horizontal_check.append(soduku_file[vertical][horizontal]) #add the number the list if not in the list
            continue
    

for horizontal in range(9):
    vertical_check=[]
    for vertical in range(9):
        if soduku_file[vertical][horizontal] in vertical_check: #if the number is in the list, there is more than one of that number in the line
            real_soduku=False
        else:
            vertical_check.append(soduku_file[vertical][horizontal]) #add the number the list if not in the list
            continue        
        

def soduku_block_counter(soduku_grid,vertical_position,horizontal_position):
    
    block_total=0
    
    for vertical in range(vertical_position-3,vertical_position):
        for horizontal in range(horizontal_position-3,horizontal_position):
            block_total+=int(soduku_grid[vertical][horizontal]) #summating all the numbers in the block
    if block_total!=45: #if the sum of a block is 45 the values must all be different
        return 1 #the section is from a real soduku grid
    else: return 0 #the grid is not a real soduku grid
 
block_checker=0 
    
for check_vertical in range(3,10,3):
    for check_horizontal in range(3,10,3):
        block_checker+=soduku_block_counter(soduku_file,check_vertical,check_horizontal) #if value > 0 then at least one of the blocks dont match up with a real soduku grid
        
        
if real_soduku==False or block_checker>0:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")