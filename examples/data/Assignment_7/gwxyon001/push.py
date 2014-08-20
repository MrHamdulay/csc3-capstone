'''Yongama Giwu
Date: 01 May 2014
Computer Science Assignment 7'''


def push_up(grid):
    for col in range(4):
        up_list=[]
        for row in range(4):
            if grid[row][col]>0:
                up_list.append(grid[row][col])
        for i in range(4-len(up_list)):
            up_list.append(0)

        for j in range(3):
             if up_list[j]==up_list[j+1]:
                  up_list[j]=up_list[j+1]*2
                  up_list[j+1]=0

        up_list1=[]
        for row in range(4):
            if up_list[row]>0:
                up_list1.append(up_list[row])
        for i in range(4-len(up_list1)):
            up_list1.append(0)



        for row_count in range(4):
            grid[row_count][col]=up_list1[row_count]

    return grid


def push_down(grid):
    for col in range(4):
        up_list=[]
        for row in range(4):
            if grid[row][col]>0:
                up_list.append(grid[row][col])
        for i in range(4-len(up_list)):
            up_list.append(0)

        for j in range(3):
             if up_list[j]==up_list[j+1]:
                  up_list[j]=up_list[j+1]*2
                  up_list[j+1]=0
        for i in range(3):
            if up_list[i]==0:
                up_list[i]=up_list[i+1]
                up_list[i+1]=0
        new_list=[]
        for i in range(4):
            if up_list[i]==0:
                new_list.append(0)
        for i in range(4-len(new_list)):
            if up_list[i]>0:
                new_list.append(up_list[i])

        for row_count in range(3,-1,-1):
            grid[row_count][col]=new_list[row_count]
    return grid




def push_left(grid):
    for row in range(4):
        row_list=[]
        for col in range(4):
            if grid[row][col]>0:
                row_list.append(grid[row][col])
        for i in range(4-len(row_list)):
            row_list.append(0)


        for j in range(3):
            if row_list[j]==row_list[j+1]:
                row_list[j]=row_list[j+1]*2
                row_list[j+1]=0
        row_list1=[]
        for col in range(4):
            if row_list[col]>0:
                row_list1.append(row_list[col])
        for i in range(4-len(row_list1)):
            row_list1.append(0)

        for count in range(4):
            grid[row][count]=row_list1[count]

    return grid



def push_right(grid):
    for row in range(4):
        row_list=[]
        for col in range(4):
            if grid[row][col]>0:
                row_list.append(grid[row][col])
        for i in range(4-len(row_list)):
            row_list.append(0)

        for j in range(3):
            if row_list[j]==row_list[j+1]:
                row_list[j]=row_list[j+1]*2
                row_list[j+1]=0
        row_list1=[]
        for col in range(4):
            if row_list[col]>0:
                row_list1.append(row_list[col])
        for i in range(4-len(row_list1)):
            row_list1.append(0)

        new_list=[]
        for i in range(4):
            if row_list1[i]==0:
                new_list.append(0)
        for i in range(4-len(new_list)):
            if row_list1[i]>0:
                new_list.append(row_list1[i])

        for count in range(4):
            grid[row][count]=new_list[count]

    return grid






































