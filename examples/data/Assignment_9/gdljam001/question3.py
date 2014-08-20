"""James Godlonton
Sodoku solution checker
10 May 2014"""

def checkValidlin(line):
    """Function that input a 9 long list and checks if its sudoku valid"""
    retBool=True
    for i in range (1,10):
        if str(i) not in line:#Check if every number form 1-9 is in the list, if they all are then its valid
            retBool=False
    return retBool#Returns T/F depending on validity of list

def checkValid():
    """Main function that inputs a sudoku block of numbers then checks if it is a valid solution"""
    arrOfLines=[]
    for i in range(9):#get 9 inputs, one for each line and add them to a list
        inpt=input("")
        arrOfLines.append(list(inpt))
    isValid=True
    for x in range(9):#Goes through each line in the list and checks if they are valid
        if  checkValidlin(arrOfLines[x]) is False:
            isValid=False
    for y in range(9):
        #Goes through the corresponding number in each line (list element) adds to an array then checks if valid
        #This essentially checks if the vertical columns are valid
        tempAr=[]
        for f in range(9):
            tempAr.append(arrOfLines[y][f])
        if checkValidlin(tempAr) is False:
            isValid=False
            
    for xCod in range (0,7,3):#goes through vals 1,3,6
        for yCod in range (0,7,3):#goes through vals 1,3,6
            #The above 2 loops allows one to start at the top left corner of each 3x3 block
            tempArr=[]
            for xBl in range (3):
                for yBl in range(3):
                    #These 2 loops go through all values in the current 3x3 block add them to an array and then checks if they are a valid combo
                    tempArr.append(arrOfLines[xCod+xBl][yCod+yBl])
            if checkValidlin(tempArr) is False:
                isValid=False
    if isValid:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
                    
    
            
        
    
    
    
if __name__=="__main__":
    checkValid()
                             
    
    
    
    
    