'''Sudoku validity checker
Reece Gounden
GNDREE002'''
def main():
    #Define variables
    gridl = []
    gridco = []
    cnt = 0
    
        #Receive and put input into list
    for i in range(9):
        tempstr = input()
        
        for i in range(9):
            gridl.append((tempstr[i]))
                
        #Create coordinates of each value
    for j in range(9):
        for i in range(9): 
            #Puts value,row,column into gridco
            gridco.append([gridl[cnt],i+1,0-j])
            cnt+=1
                
    if CheckValid(gridco,gridl):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

#Function to check validity of rows
def CheckValid(grid_co,grid_l):
    cnt2 = 0
    valid = False
    rowi = []
    columni = []
    subgridi = []
    
    for i in range(9):
        for j in range(9):
            if grid_co[j][1] == i:
                rowi.append(grid_co[j][0])
            else:
                pass
        for k in range(9):
            if grid_co[j][0] in rowi:
                valid = False
            else: 
                valid = True
    
        #Check if columns are valid
    for i in range(9):
            for j in range(9):
                if grid_co[i][2] == i:
                    columni.append(grid_co[i][0])
                else:
                    pass
            for k in range(9):
                if grid_co[i][0] in columni:
                    valid = False
                else: 
                    valid = True   
                        
        #Splits gridl into sub grid 
    for l in range(81)[::27]:
        for k in range(9)[::3]:
            del subgridi[:]
            for i in range(27)[::9]:
                for j in range(3):
                    subgridi.append(grid_l[i+j+k+l])
                
    # Check validity of sub-grid i            
            for m in range(9):
                cnt2 = 0
                for n in range(9):
                    if subgridi[m]==subgridi[n]:
                        cnt2 += 1
                    else: 
                        pass
                if cnt2 > 1:
                    valid = False
                    break
                else:
                    pass
    return valid

main() 