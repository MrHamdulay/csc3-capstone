#Tayla Radmore
#12 May 2014
# checking a sudoku grid is valid
answer=""
list_of_nine_numbers=[]
final_list=[]
block=[]
for i in range (9):
    nine_numbers=input("")
    
    for i in range(9):
        list_of_nine_numbers.append(nine_numbers[i])
    final_list.append(list_of_nine_numbers)
    list_of_nine_numbers=[]

for x in range(9):    
    for y in range(9):    
        for i in range(9):
            
            if y!=i:
                if final_list[x][y]==final_list[x][i]:
                    answer="false"


for x in range(9):
    for y in range(9):
        for i in range(9):
            if y!=i:
                if final_list[y][x]==final_list[i][x]:
                    answer="false"


def block_create(row,colum):                    
    for x in range(row):
        for y in range(colum):
            block.append(final_list[x][y])
            
    return block
        
        
block_create(3,3)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
                    
block_create(6,3)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
                    
block_create(9,3)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
    
block_create(3,6)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
    
block_create(6,6)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
    
block_create(9,6)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
    
block_create(3,9)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
                    
block_create(6,9)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
                    
    
block_create(9,9)
for z in range(9):
        for a in range(9):
            if z!=a:
                if block[z]==block[a]:
                    answer="false"
    
                    
    
                    
    
                    

        
        
        
        
        
        
        
        
        
        
        









if answer=="false":
    print("Sudoku grid is not valid")
    
else:
    print("Sudoku grid is valid")
    