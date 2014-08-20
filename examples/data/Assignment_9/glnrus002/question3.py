#GLNRUS002
#ASSIGNMENT 9
#QUESTION 3
#SUDOKU VALIDIFYING PROGRAM

grid=0 #used for vertical counting of grids of 3x3
block=0#horizontal
inspect=0#used as a value to see if enough conditions have been met

def horizontal_check(s):#performs horizontal check
    tester="123456789"#used to identify unique characters
    flag =True#innocent until proven guilty
    for i in s:#line in array
        for j in i:#individual character in line
            if j in tester:#if certain character in range of tester
                tester=tester.replace(str(j),"0")#remove j test case
            else:
                flag=False
        tester="123456789"#reset tester
    return flag

def vertical_check(s):#performs vertical check   
    tester="123456789"#used for removing unique characters
    flag=True#innocent until proven otherwise
    single=len(s[0])#get length of only one line in s
    for j in range(single-1):
        for i in s:#line in array
            if i[j] in tester:
                tester=tester.replace(str(i[j]),"0")
            else:
                flag=False
        tester="123456789"#reset tester
    return flag

def grid_check(s):#checks 3x3 blocks
    global grid#gets "global" values
    global block
    global inspect
    if inspect==9:#if all nine blocks has been checked and the flag is still set on true
        return True
    flag=True#used as the eternal flag
    tmp=""#used to build a single string of the 3x3 grid
    
    for i in range(grid,3+grid):#y-co ordinate. Grid moves us one block of 3x3 DOWN
       
        for j in range(block,3+block):#xCo ordinate. Block moves us one block of 3x3 RIGHT
            tmp=tmp+s[i][j]#builds string for testing
    flag=horizontal_check(tmp)#once string has been built of a whole 3x3 block, perform the standard horizontal line check for uniqueness
    tmp=""#reset tmp so that we can start building a string for the next 3x3 block
    grid +=3#shift to block below
    if grid<=6:#if there is still blocks below
        if flag==True:#check if sudoku has not been spoilt and thus can just return false
            inspect+=1#add one to the total used to check if still true after all tests
            grid_check(s)#rerun this method
        else:
            return False
    else:
        block+=3#move right one
        grid=0#move back to top
        inspect+=1#add brownie points
        grid_check(s)#do check on next block

if __name__=="__main__":
######get input######################    
    count =0
    sudoku=[]
    while count<9:
        sudoku.append(input())
        count+=1
    horizontal_check(sudoku)
    check=True#used to check if all tests can be proven true    
    check=horizontal_check(sudoku)
    if check== False:
        print("Sudoku grid is not valid")
    else:#check meets first criterion
        check=vertical_check(sudoku)
        if check==False:
            print("Sudoku grid is not valid")
        else:#meets second criterion
            check=grid_check(sudoku)
            if check!=True:
                print("Sudoku grid is valid")
            else:
                print("Sudoku grid is not valid")