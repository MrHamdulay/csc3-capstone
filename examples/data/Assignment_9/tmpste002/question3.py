""" Check if a complete Sudoku grid is valid or not """
__author__ = 'Stephen Temple'
__date__ = '2014/05/12'


def check_rows(grid):
    """ Look for repeated numbers in a row """
    for row in grid:
        # array of numbers 1 to 9
        numbers = [str(i) for i in range(1, 10)]
        for n in row:
            if n in numbers:
                numbers.remove(n)  # if number found remove from numbers array
            else:
                return False
    return True


def check_columns(grid):
    """ Look for repeated numbers in a column """
    for col in range(len(grid)):
        # array of numbers 1 to 9
        numbers = [str(i) for i in range(1, 10)]
        for row in range(len(grid)):
            if grid[row][col] in numbers:
                numbers.remove(grid[row][col])  # if number found remove from numbers array
            else:
                return False
    return True


def check_3by3(grid):
    """ Look for repeated numbers in 3x3 grid """
    for h_start in [0, 3, 6]:
        for v_start in [0, 3, 6]:
            # array of numbers 1 to 9
            numbers = [str(i) for i in range(1, 10)]
            for h_inc in [0, 1, 2]:
                for v_inc in [0, 1, 2]:
                    if grid[0 + h_start + h_inc][0 + v_start + v_inc] in numbers:
                        numbers.remove(grid[0 + h_start + h_inc][0 + v_start + v_inc])
                    else:
                        return False
    return True


def main():
    grid = []
    for i in range(9):
        grid.append(input(''))

    if check_rows(grid) and check_columns(grid) and check_3by3(grid):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")


if __name__ == '__main__':
    main()