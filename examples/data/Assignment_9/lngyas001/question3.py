"""program to check if a completed sudoku grid is valid
yasha longstaff
15 may 2014"""

def sudoku():
# creating rows
        r1 = list(input())
        r2 = list(input())
        r3 = list(input())
        r4 = list(input())
        r5 = list(input())
        r6 = list(input())
        r7 = list(input())
        r8 = list(input())
        r9 = list(input())
        
        
        #creating columns
        c1 = [r1[0],r2[0],r3[0],r4[0],r5[0],r6[0],r7[0],r8[0],r9[0]]
        c2 = [r1[1],r2[1],r3[1],r4[1],r5[1],r6[1],r7[1],r8[1],r9[1]]
        c3 = [r1[2],r2[2],r3[2],r4[2],r5[2],r6[2],r7[2],r8[2],r9[2]]
        c4 = [r1[3],r2[3],r3[3],r4[3],r5[3],r6[3],r7[3],r8[3],r9[3]]
        c5 = [r1[4],r2[4],r3[4],r4[4],r5[4],r6[4],r7[4],r8[4],r9[4]]
        c6 = [r1[5],r2[5],r3[5],r4[5],r5[5],r6[5],r7[5],r8[5],r9[5]]
        c7 = [r1[6],r2[6],r3[6],r4[6],r5[6],r6[6],r7[6],r8[6],r9[6]]
        c8 = [r1[7],r2[7],r3[7],r4[7],r5[7],r6[7],r7[7],r8[7],r9[7]]
        c9 = [r1[8],r2[8],r3[8],r4[8],r5[8],r6[8],r7[8],r8[8],r9[8]]
        
        # creating 3x3 block lists
        b1 = [r1[0],r1[1],r1[2],r2[0],r2[1],r2[2],r3[0],r3[1],r3[2]]
        b2 = [r1[3],r1[4],r1[5],r2[3],r2[4],r2[5],r3[3],r3[4],r3[5]]
        b3 = [r1[6],r1[7],r1[8],r2[6],r2[7],r2[8],r3[6],r3[7],r3[8]]
        b4 = [r4[0],r4[1],r4[2],r5[0],r5[1],r5[2],r6[0],r6[1],r6[2]]
        b5 = [r4[3],r4[4],r4[5],r5[3],r5[4],r5[5],r6[3],r6[4],r6[5]]
        b6 = [r4[6],r4[7],r4[8],r5[6],r5[7],r5[8],r6[6],r6[7],r6[8]]
        b7 = [r7[0],r7[1],r7[2],r8[0],r8[1],r8[2],r9[0],r9[1],r9[2]]
        b8 = [r7[3],r7[4],r7[5],r8[3],r8[4],r8[5],r9[3],r9[4],r9[5]]
        b9 = [r7[6],r7[7],r7[8],r8[6],r8[7],r8[8],r9[6],r9[7],r9[8]]
        
        # merging the lists
        numbers = ["1","2","3","4","5","6","7","8","9"]
        rows = [r1,r2,r3,r4,r5,r6,r7,r8]
        columns = [c1,c2,c3,c4,c5,c6,c7,c8,c9]
        blocks = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
        
        test_variable = 0
        # check columns
        for character in columns:
                for number in numbers:
                        if character.count(number) != 1:
                                test_variable += 1
        
        # check rows 
        for character in rows:
                for number in numbers:
                        if character.count(number) != 1:
                                test_variable += 1
        
        #check 3x3 blocks
        for character in blocks:
                for number in numbers:
                        if character.count(number) != 1:
                                test_variable += 1
        
        # test to see if grid is valid
        if test_variable == 0:
                print("Sudoku grid is valid")
        else:
                print("Sudoku grid is not valid")
                
sudoku()