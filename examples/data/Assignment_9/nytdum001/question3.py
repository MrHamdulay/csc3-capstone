"""Program to test validity of sudoku grid
Dumisani J Nyathi
18-05-2014"""

#Sudoku grid
me = [[3,5,9],[7,1,6],[4,8,2],
       [8,6,7],[3,4,5],[9,1,2],
        [4,1,3],[9,2,8],[6,7,5],
        [3,9,8],[5,7,4],[1,2,6],
        [5,4,6],[2,8,1],[7,3,9],
        [1,7,2],[6,3,9],[5,4,8],
        [9,8,4],[1,6,2],[2,5,7],
        [6,2,1],[8,5,7],[3,9,5],
        [7,3,5],[4,9,2],[8,6,3]]


#Create a list to hold the rows
row = []

#append the sudoku numbers into the row list in 3 by 3
for i in me:
    for k in range(3):
        row.append(i[k])


#For the 9 rows of the sudoku grid create 9 lists
r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []


#create a dictionary of the rows to associate to the main lists
dic = {"r1" : r1, "r2" : r2, "r3" : r3, "r4" : r4, "r5" : r5, "r6" : r6, "r7" : r7, "r8" : r8, "r9" : r9}

#divide the sudoku grid into 9 by 9 ranges.
s = range(0,90,9)

#in each range of 9, append the sudoku number to its relevant row
for k in s:
    if k == 9:
        for l in range(k):
            r1.append(row[l])
    elif k == 18:
        for l in range(9, k):
            r2.append(row[l])
    elif k == 27:
        for l in range(18, k):
            r3.append(row[l])
    elif k == 36:
        for l in range(27, k):
            r4.append(row[l])
    elif k == 45:
        for l in range(36, k):
            r5.append(row[l])
    elif k == 54:
        for l in range(45, k):
            r6.append(row[l])
    elif k == 63:
        for l in range(54, k):
            r7.append(row[l])
    elif k == 72:
        for l in range(63, k):
            r8.append(row[l])
    elif k == 81:
        for l in range(72, k):
            r9.append(row[l])


#Create a function to work on the sudoku grid row by row, column by column and 3x3 box
def Validitiy(dict):
    #create a validity check by using a base 0 to count of errors encountered
    valid = 0
    #Create lists and dictionary of 3x3 boxes to work on
    box1 = []
    box2 = []
    box3 = []
    box4 = []
    box5 = []
    box6 = []
    box7 = []
    box8 = []
    box9 = []
    boxes = {
            "box1":box1,
            "box2":box2,
            "box3":box3,
            "box4":box4,
            "box5":box5,
            "box6":box6,
            "box7":box7,
            "box8":box8,
            "box9":box9}
    #Create a lists and dictionary of columns to check validity
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    col5 = []
    col6 = []
    col7 = []
    col8 = []
    col9 = []
    columns = {"col1":col1,
            "col2":col2,
            "col3":col3,
            "col4":col4,
            "col5":col5,
            "col6":col6,
            "col7":col7,
            "col8":col8,
            "col9":col9}


    #Using the for loop to loop throught the dictionary keys. the values are in lists of sudoku numbers
    #for each column, append the number associated with the position of the column
    #for each box, append the 3 numbers into the list based on the position of the boxes
    for key in dic.keys():
        w = dic[key]
        col1.append(w[0])
        col2.append(w[1])
        col3.append(w[2])
        col4.append(w[3])
        col5.append(w[4])
        col6.append(w[5])
        col7.append(w[6])
        col8.append(w[7])
        col9.append(w[8])
        #Append into boxes lists using the list method "extend", the first box will get the first three numbers of the first three rows and so on
        if key == "r1":
            box1.extend(w[:3])
            box2.extend(w[3:6])
            box3.extend(w[6:9])
        elif key == "r2":
            box1.extend(w[:3])
            box2.extend(w[3:6])
            box3.extend(w[6:9])
        elif key == "r3":
            box1.extend(w[:3])
            box2.extend(w[3:6])
            box3.extend(w[6:9])
        elif key == "r4":
            box4.extend(w[:3])
            box5.extend(w[3:6])
            box6.extend(w[6:9])
        elif key == "r5":
            box4.extend(w[:3])
            box5.extend(w[3:6])
            box6.extend(w[6:9])
        elif key == "r6":
            box4.extend(w[:3])
            box5.extend(w[3:6])
            box6.extend(w[6:9])
        elif key == "r7":
            box7.extend(w[:3])
            box8.extend(w[3:6])
            box9.extend(w[6:9])
        elif key == "r8":
            box7.extend(w[:3])
            box8.extend(w[3:6])
            box9.extend(w[6:9])
        elif key == "r9":
            box7.extend(w[:3])
            box8.extend(w[3:6])
            box9.extend(w[6:9])

    #Using the set data structure, takes all the values in a list with no duplicate elements. a valid sudoku grid row,column or box will have 9 elements
    #The set data structure will determine the number of elements in a list. if the count is not equal to 9. the sudoku grid is not valid
    for key in dic.keys():
        w = dic[key]
        x = set(w)
        #anytime valid check is wrong the number of errors will increase, this will determin the end result
        if len(x) == 9:
            valid += 0
        else:
            valid += 1

    for key in columns.keys():
        c = columns[key]
        y = set(c)
        if len(y) == 9:
            valid += 0
        else:
            valid += 1

    for key in boxes.keys():
        h = boxes[key]
        f = set(h)
        if len(f) == 9:
            valid += 0
        else:
            valid += 1

    #if no duplicates found valid will remain 0, else it will increase
    if valid == 0:
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")




Validitiy(dic)