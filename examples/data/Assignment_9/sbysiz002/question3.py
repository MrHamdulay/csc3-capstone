"""Sizwe Sibiya
Assignment 10"""

def main():
    #Defining
    gridl = []
    gridco = []
    count = 0
    count2 = 0
    valid = 'FALSE'
    rowi = []
    columni = []
    subgridi = []
    
    
    #Take input from user and put it in a list
    for i in range(9):
        tempstr = input()
        
        for i in range(9):
            gridl.append((tempstr[i]))
            
    #Find the coordinates of each value
    for j in range(9):
        for i in range(9):
            #[value,row,column]
            gridco.append([gridl[count],i+1,0-j])
            count += 1
            
    #Validity of rows
    for i in range(9):
        for j in range(9):
            if gridco[j][1] == i:
                rowi.append(gridco[j][0])
            else:
                pass
        for k in range(9):
            if gridco[j][0] in rowi:
                valid = 'FALSE'
            else: 
                valid = 'TRUE'

    #Check validity of columns
    for i in range(9):
            for j in range(9):
                if gridco[i][2] == i:
                    columni.append(gridco[i][0])
                else:
                    pass
            for k in range(9):
                if gridco[i][0] in columni:
                    valid = 'FALSE'
                else: 
                    valid = 'TRUE'   
                    
    #Divide grid-l into sub-grid i
    for l in range(81)[::27]:
        for k in range(9)[::3]:
            del subgridi[:]
            for i in range(27)[::9]:
                for j in range(3):
                    subgridi.append(gridl[i+j+k+l])
            
#Validity of sub-grid i            
            for m in range(9):
                count2 = 0
                for n in range(9):
                    if subgridi[m]==subgridi[n]:
                        count2 += 1
                    else: 
                        pass
                if count2 > 1:
                    valid = 'FALSE'
                    break
                else:
                    pass
    
    if valid == 'TRUE':
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
main()
    