def no_duplicates(_list):
    if len(_list) == len(set(_list)):
        return True
    else:
        return False

def row_maker(text):
    line = []
    for i in text:
        line.append(eval(i))
    return line
    
def row_list(text_lines):
    lines_list = []
    for i in text_lines:
        line = row_maker(i)
        lines_list.append(line)
    return lines_list

def no_duplicates_2d(_list):
    for i in _list:
        if no_duplicates(i) == False:
            return False
    return True

def column_list(_list):
    list_columns = []
    for i in range(len(_list)):
        column = []
        for row in _list:
            column.append(row[i])
        list_columns.append(column)
    return list_columns

def subgrid_third(_list):
    """creates 3 3x3 arrays from a 3x9 array"""
    subgrid_list = []
    for i in range(0,9,3):
        subgrid = []
        for y in range(3):
            for x in range(3):
                subgrid.append(_list[x][i+y])
        subgrid_list.append(subgrid)
    return subgrid_list

def subgrid_list(_list):
    """creates a list of non overlapping 3x3 arrays from a 9x9 array of rows"""
    list1 = subgrid_third(_list[0:3])
    list2 = subgrid_third(_list[3:6])
    list3 = subgrid_third(_list[6:])
    
    for i in range(3):
        list1.append(list2[i])
        list1.append(list3[i])
        
    return list1
    
    
def main():
    line_list = []
    
    for row in range(9):
        row = input()
        line_list.append(row)
        
    rows = row_list(line_list)
    columns = column_list(rows)
    subgrids = subgrid_list(rows)
    
    if no_duplicates_2d(rows) == True and no_duplicates_2d(columns) == True and no_duplicates_2d(subgrids) == True:
        print('Sudoku grid is valid')
        
    else:
        print('Sudoku grid is not valid')

main()
        