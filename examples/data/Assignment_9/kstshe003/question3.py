#sheldon kisten
#16 may 2014
#question 3

def check_sudoku(x):
    value = len(x)
    for row in x:
        #check that len(row) == len(x)
        # so we know we have a square
        if len(row) != len(x):
            return print("Sudoku grid is not valid")
    for row in x:
        # For each thing in each row of x
        # check that said thing is not greater
        # than len(x) and also that thing is
        # not a float.
        for thing in row:
            if thing>len(x):
                return print("Sudoku grid is not valid")
            elif isinstance(thing,float) or thing<1:
                return print("Sudoku grid is not valid")
    # Cycle through value at increments of -1
    # checking that thing does not occur more
    # than once per row
    while value>0:
        for row in x:
            for thing in row:
                if row.count(thing) > 1:
                    return print("Sudoku grid is not valid")
                else:
                    value-=1
    # Check for recurrences per column
    value = len(x)
    eachRow = []
    # While value is greater than 0, cycle through
    # each row of x, appending whatever is at
    # row[value-1] to the list eachRow.
    # Check that thing does not occur more than once
    # per column and that thing is not a float.
    while value>0:
        for row in x:
            eachRow.append(row[value-1])
        for thing in eachRow:
            if thing > len(x):
                return print("Sudoku grid is not valid")
            elif eachRow.count(thing) > 1:
                return print("Sudoku grid is not valid")
            elif isinstance(thing,float) or thing<1:
                return print("Sudoku grid is not valid")
            else:
                eachRow = []
                value-=1
        return print("Sudoku grid is valid")
    
x=input("")
check_sudoku(x)