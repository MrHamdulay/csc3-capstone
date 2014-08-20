"""program to check if complete sudoku 
vicky stark
14 may 2014"""

#create a list with the sudoku lines
grid=[]
numbers=input()
grid.append(numbers)
for i in range(8):
        numbers=input()
        grid.append(numbers)
        

#variables. Outcome will be used as an overall indicator as to whether the sudoku grid is valid. Let outcome = True from the start. True=correct 
outcome=True
counter=0
              
#to check that no 3x3 grid has the same value
#we are going through each line, and taking the 1st 3, 2nd 3 and 3rd 3 letters and adding them to their respective blocks, then looping through that so that at the end the 1st three horizontal blocks have been written into a list as one string for each block

small_grid=[] #a list which has all the 3x3 block values as one item in the list
row_number=0
number='' #the current number
count=9
block_1='' #the blocks refer ot the 3x3 grids in the 9x9 array
block_2=''
block_3=''
while count > 0:
        number = grid[row_number]
        block_1+=number[0:3]
        block_2+=number[3:6]
        block_3+=number[6:9]
        row_number+=1
        count-=3
small_grid.append(block_1)
small_grid.append(block_2)
small_grid.append(block_3)
                
#we are going through each line, and taking the 1st 3, 2nd 3 and 3rd 3 letters and adding them to their respective blocks, then looping through that so that at the end the 2nd three horizontal blocks have been written into a list as one string for each block

row_number=3
number='' #the current number
count=9
block_1=''
block_2=''
block_3=''
while count > 0:
        number = grid[row_number]
        block_1+=number[0:3]
        block_2+=number[3:6]
        block_3+=number[6:9]
        row_number+=1
        count-=3
small_grid.append(block_1)
small_grid.append(block_2)
small_grid.append(block_3)
                
#we are going through each line, and taking the 1st 3, 2nd 3 and 3rd 3 letters and adding them to their respective blocks, then looping through that so that at the end the 3rd three horizontal blocks have been written into a list as one string for each block

row_number=6
number='' #the current number
count=9
block_1=''
block_2=''
block_3=''
while count > 0:
        number = grid[row_number]
        block_1+=number[0:3]
        block_2+=number[3:6]
        block_3+=number[6:9]
        row_number+=1
        count-=3
small_grid.append(block_1)
small_grid.append(block_2)
small_grid.append(block_3)
                        
#check for any values that are the same in the 3x3 blocks

for lets in small_grid:
        for i in lets:
                no_of_occurances = lets.count(i)
                if no_of_occurances  > 1:
                        outcome= False
                        break
 
#to check that no 2 cells in the same row have the same value
for i in grid:
        for number in i:
                counter=i.count(number) 
                if counter != 1:
                        outcome=False 
                        #we don't need to keep checking the values if one of them is false, and so we can break out of loop
                        break 
                

#to check that no 2 cells in the same coloumn have the same value
letters=[]
digits=[]
for number in grid:
        digits.append(number)
        
for i in range(len(digits)-1):
        for letter in grid:
                letters.append(letter[i])
        
for i in range(9):
        for j in range(8):
                if digits[i]== letters[j+1]:
                        outcome=False
                        #we don't need to keep checking the values if on of them is false, and so we can break out of loop
                        break               
#FINAL check
if outcome == True:
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")