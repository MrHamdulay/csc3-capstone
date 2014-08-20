"""Files: checking if a sudoku grid is valid or not
danica van der zandt
11 may 2014"""

#get input and saving it into a list of nine items that are given
lines=[]
given_grid=input()
while given_grid:
    lines.append(given_grid)
    given_grid=input()
    

#overwrite any file that may already exist with the list of nine elements
f=open("sudoku_grid.txt","w")
print(lines, file=f)
f.close()

#for column values
#putting all the numbers going down a column into a long string to be checked
col=""
for counter in range(9):
    for line in lines:
        col+=line[counter]
    col+=","

#splitting the string into a list of elements
col_values=col.split(",")
col_values=col_values[:len(col_values)-1]
#print(col_values)
 
#for 3x3 values 
#putting all the numbers going down a 3 width column into a long string to be checked
blocks=""
counter=0

for segment in range(0,9,3):
    for line in lines:
        blocks+=line[counter:counter+3]
    counter+=3
    blocks+=","    
       
#splitting the blocks string into a list of 3 elements
blocks=blocks.split(",")
blocks=blocks[:len(blocks)-1]

#splitting the blocks into a list of 9 elements
nine_blocks=[]
for ablock in blocks:
    nine_blocks.append(ablock[0:9])
    nine_blocks.append(ablock[9:18])
    nine_blocks.append(ablock[18:27]) 
 
    
#checking for duplicates in the three cases

#check if a number from 1 - 9 DOESN'T appear in the items of the list
numbers=["1","2","3","4","5","6","7","8","9"]

#checking the original items (rows)
cts=0
for row in lines:
    for integer in numbers:
        if integer not in row:
            print("Sudoku grid is not valid.")
            cts+=1
            break
        if cts:
            break
        else:
            continue
        
    
        
        
#checking the items in the column values

if cts:
    False
else:
    for acol in col_values:
        for integer in numbers: 
            if integer not in acol: 
                print("Sudoku grid is not valid.")
                cts+=1
                break
        if cts:
            break
        else:
            continue
        
                
#checking items in 3x3 segments
if cts==1:
    False
else:
    for triplet in nine_blocks:
        for integer in numbers:
            if integer not in triplet:
                print("Sudoku grid is not valid.")
                break
            else:
                print("Sudoku grid is valid.")
                break
        break
    

    
          


    
    
#print(blocks)


