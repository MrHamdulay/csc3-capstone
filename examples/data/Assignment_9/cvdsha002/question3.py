"""Shahrain Coovadia"""

list=[]    #create empty list for grid
grid1=''         #create a holder
cont1='no'         #creates continuation/stopping clauses
cont2 ='yes'       
b=0
while len (list)<9:   
    list.append(input())     #add input to list 

for i in range(9):
    if str(1+i) in list[i]:    #checks if number has occurred 
        cont1='yes'
        
for j in range(9):             
    if cont2 =='yes':
        for k in range(9):
            grid1+=list[k][j]  #add numbers to grid
            
        for l in range(1,10):       #checks if number has occurred
            if str(l) in grid1: 
                cont2=='yes'
            else:               
                cont2='no'            
                break
    grid1=''
                
    if cont2=='no':
        break
    
if (cont1=='yes' and cont2=='yes'):
    print("Sudoku grid is valid")    #output
else:
    print("Sudoku grid is not valid")