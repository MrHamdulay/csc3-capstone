#this program checks if the sudoko is valid or not
#
#10 MAY 2014


#get input
data=[]
while len(data)<9:
    x=input()
    data.append(list(x))

#change values in a the array to int data type
for i in range(9):
    for j in range(9): 
        data[i][j]=eval(data[i][j])

def check(data):
    """checks if the sudoku is correct of not"""
    for i in data:
        I=[]
        for j in range(9):
            I.append(i[j])
        I.sort()
        if I==[1,2,3,4,5,6,7,8,9]: 
            continue
        else: return False

    for j in range(9):
        temp=[]
        for i in data:    
            temp.append(i[j])
        temp.sort()
        if temp==[1,2,3,4,5,6,7,8,9]:
            continue
        else: 
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            temp=[]
            for k in range(3):
                for l in range(3):
                    temp.append(data[i+k][j+l])
            temp.sort()
            if temp==[1,2,3,4,5,6,7,8,9]:
                continue
            else: return False
    return True
#data=[3,5,9,7,1,6,4,8,2],[8,6,7,3,4,5,9,1,2],[4,1,3,9,2,8,6,7,5],[3,9,8,5,7,4,1,2,6],[5,4,6,2,8,1,7,3,9],[1,7,2,6,3,9,5,4,8],[9,8,4,1,6,3,2,5,7],[6,2,1,8,5,7,3,9,4],[7,3,5,4,9,2,8,6,1]
check_value=check(data)


#return output
if check_value:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")