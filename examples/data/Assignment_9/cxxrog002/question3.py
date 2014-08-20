""" check if a soduko is correct or not
Roger Cox
15 may 2014 """

array=[] # makes a 2 D array with all values given
for i in range(9):
        x=input("")
        line = []
        for y in str(x):
                line.append(y)
        array.append(line)
        
        
                              
def check_verticle():
     # make a verticle array
        verticle=[]
        y=0
        x=0
        for i in range(9):
                verticle.append(["0"]*9)                           
                
        for x in range(9):
                count=0
                for lines in array :
                        verticle[y][count]=lines[y]
                        count+=1
                       
                y+=1
                
        return(verticle)       
        # return the array verticle
verticle=check_verticle()


def check_numbers(verticle):
        # this checks the array and verticle for duplicates
        for line in verticle:
                line= sorted(line, key=int) # sorts line 1,2,3,4,5,6,7,8,9
                x=1
                for i in range(len(line)):    
                        if x == eval(line[i]):
                                
                                x+=1                 
                        else:
                                return False
                        
        return True


def checkcell(array):
        # checks one cell is correct
        sumd=0
        for i in range (3):
                sumd+=eval(array[0][i]) 
                sumd+=eval(array[1][i])
                sumd+=eval(array[2][i])
                

        if sumd !=45 :
                return False
        else:
                return True


        
        
def check_everything(array,verticle) :
        # if all the tests are true soduko is correct
        if check_numbers(verticle) and check_numbers(array) and (checkcell(array)  ):
                print("Sudoku grid is valid")
        else:
                print("Sudoku grid is not valid")

check_everything(array,verticle)
