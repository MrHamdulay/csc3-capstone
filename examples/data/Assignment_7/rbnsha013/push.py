"""2048 game
Shane Robinson
27 April 2014"""

import util

def push_up(grid):
    """merge grid values upwards"""
    for i in range(4):
        for j in range(4):
            if i==0:
                continue
            elif i==1:
                if grid[i][j]==0:
                    continue
                elif grid[i-1][j]!=0:
                    if grid[i][j]==grid[i-1][j]:
                        grid[i-1][j] = grid[i][j]+grid[i-1][j]
                        grid[i][j] = 0
                    elif grid[i][j]!=grid[i-1][j]:
                        continue
                elif grid[i-1][j]==0:
                    grid[i-1][j] = grid[i][j]
                    grid[i][j] = 0
            elif i==2:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i-2][j]==0:
                        if grid[i-1][j]==0:
                            grid[i-2][j] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i-1][j]==grid[i][j]:
                            grid[i-2][j] = grid[i-1][j]+grid[i][j]
                            grid[i-1][j] = 0
                            grid[i][j] = 0
                        elif grid[i-1][j]!=grid[i][j]:
                            grid[i-2][j] = grid[i-1][j]
                            grid[i-1][j] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i-2][j]!=0 and grid[i-1][j]!=0:
                        if grid[i-2][j]==grid[i-1][j]:
                            grid[i-2][j] = grid[i-2][j]+grid[i-1][j]
                            grid[i-1][j] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i-2][j]!=grid[i-1][j]:
                            if grid[i-1][j]==grid[i][j]:
                                grid[i-1][j] = grid[i-1][j]+grid[i][j]
                                grid[i][j] = 0
                            elif grid[i-1][j]!=grid[i][j]:
                                continue
                    elif grid[i-2][j]!=0 and grid[i-1][j]==0:
                        if grid[i-2][j]==grid[i][j]:
                            grid[i-2][j] = grid[i-2][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i-2][j]!=grid[i][j]:
                            grid[i-1][j] = grid[i][j]
                            grid[i][j] = 0
            elif i==3:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i-3][j]==0:
                        if grid[i-2][j]==0:
                            if grid[i-1][j]==0:
                                grid[i-3][j] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i-1][j]!=0 and grid[i][j]!=grid[i-1][j]:
                                grid[i-3][j] = grid[i-1][j]
                                grid[i-1][j] = 0
                                grid[i-2][j] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i-1][j]!=0 and grid[i][j]==grid[i-1][j]:
                                grid[i-3][j] = grid[i][j]+grid[i-1][j]
                                grid[i][j] = 0
                                grid[i-1][j] = 0
                        elif grid[i-2][j]!=0 and grid[i-1][j]==0:
                            if grid[i-2][j]==grid[i][j]:
                                grid[i-3][j] = grid[i-2][j]+grid[i][j]
                                grid[i][j] = 0
                                grid[i-2][j] = 0
                            elif grid[i-2][j]!=grid[i][j]:
                                grid[i-3][j] = grid[i-2][j]
                                grid[i-2][j] = grid[i][j]
                                grid[i][j] = 0
                        elif grid[i-2][j]!=0 and grid[i-1][j]!=0:
                            if grid[i-2][j]==grid[i-1][j]:
                                grid[i-3][j] = grid[i-2][j]+grid[i-1][j]
                                grid[i-2][j] = grid[i][j]
                                grid[i][j] = 0
                                grid[i-1][j] = 0
                            elif grid[i-1][j]==grid[i][j]:
                                grid[i-3][j] = grid[i-2][j]
                                grid[i-2][j] = grid[i-1][j]+grid[i][j]
                                grid[i][j] = 0
                                grid[i-1][j] = 0
                            elif grid[i-2][j]!=grid[i-1][j] and grid[i-1][j]!=grid[i][j]:
                                grid[i-3][j] = grid[i-2][j]
                                grid[i-2][j] = grid[i-1][j]
                                grid[i-1][j] = grid[i][j]
                                grid[i][j] = 0
                    elif grid[i-3][j]!=0 and grid[i-2][j]==0 and grid[i-1][j]==0:
                        if grid[i-3][j]==grid[i][j]:
                            grid[i-3][j] = grid[i-3][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i-3][j]!=grid[i][j]:
                            grid[i-2][j] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i-3][j]!=0 and grid[i-2][j]!=0 and grid[i-1][j]==0:
                        if grid[i-2][j]==grid[i][j]:
                            grid[i-2][j] = grid[i-2][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i-2][j]!=grid[i][j]:
                            grid[i-1][j] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i-3][j]!=0 and grid[i-2][j]!=0 and grid[i-1][j]!=0:
                        if grid[i][j]==grid[i-1][j]:
                            grid[i-1][j] = grid[i-1][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i-1][j]==grid[i-2][j]:
                            grid[i-2][j] = grid[i-2][j]+grid[i-1][j]
                            grid[i-1][j] = 0
                        elif grid[i-3][j]==grid[i-2][j]:
                            grid[i-3][j] = grid[i-3][j]+grid[i-2][j]
                    elif grid[i-3][j]!=0 and grid[i-2][j]==0 and grid[i-1][j]!=0:
                        if grid[i-1][j]==grid[i][j]:
                            grid[i-2][j] = grid[i-1][j]+grid[i][j]
                            grid[i-1][j] = 0
                            grid[i][j] = 0
                        elif grid[i-3][j]==grid[i-1][j]:
                            grid[i-3][j] = grid[i-3][j]+grid[i-1][j]
                            grid[i-2][j] = grid[i][j]
                            grid[i-1][j] = 0
                            grid[i][j] = 0
                        elif grid[i-1][j]!=grid[i][j] and grid[i-3][j]!=grid[i-1][j]:
                            grid[i-2][j] = grid[i-1][j]
                            grid[i-1][j] = grid[i][j]
                            grid[i][j] = 0
    
def push_down(grid):
    """merge grid values downwards"""
    for i in range(4):
        for j in range(4):
            if i==0:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i+3][j]==0:
                        if grid[i+2][j]==0:
                            if grid[i+1][j]==0:
                                grid[i+3][j] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i+1][j]!=0 and grid[i][j]!=grid[i+1][j]:
                                grid[i+3][j] = grid[i+1][j]
                                grid[i+1][j] = 0
                                grid[i+2][j] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i+1][j]!=0 and grid[i][j]==grid[i+1][j]:
                                grid[i+3][j] = grid[i][j]+grid[i+1][j]
                                grid[i][j] = 0
                                grid[i+1][j] = 0
                        elif grid[i+2][j]!=0 and grid[i+1][j]==0:
                            if grid[i+2][j]==grid[i][j]:
                                grid[i+3][j] = grid[i+2][j]+grid[i][j]
                                grid[i][j] = 0
                                grid[i+2][j] = 0
                            elif grid[i+2][j]!=grid[i][j]:
                                grid[i+3][j] = grid[i+2][j]
                                grid[i+2][j] = grid[i][j]
                                grid[i][j] = 0
                        elif grid[i+2][j]!=0 and grid[i+1][j]!=0:
                            if grid[i+2][j]==grid[i+1][j]:
                                grid[i+3][j] = grid[i+2][j]+grid[i+1][j]
                                grid[i+2][j] = grid[i][j]
                                grid[i][j] = 0
                                grid[i+1][j] = 0
                            elif grid[i+1][j]==grid[i][j]:
                                grid[i+3][j] = grid[i+2][j]
                                grid[i+2][j] = grid[i+1][j]+grid[i][j]
                                grid[i][j] = 0
                                grid[i+1][j] = 0
                            elif grid[i+2][j]!=grid[i+1][j] and grid[i+1][j]!=grid[i][j]:
                                grid[i+3][j] = grid[i+2][j]
                                grid[i+2][j] = grid[i+1][j]
                                grid[i+1][j] = grid[i][j]
                                grid[i][j] = 0
                    elif grid[i+3][j]!=0 and grid[i+2][j]==0 and grid[i+1][j]==0:
                        if grid[i+3][j]==grid[i][j]:
                            grid[i+3][j] = grid[i+3][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i+3][j]!=grid[i][j]:
                            grid[i+2][j] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i+3][j]!=0 and grid[i+2][j]!=0 and grid[i+1][j]==0:
                        if grid[i+2][j]==grid[i][j]:
                            grid[i+2][j] = grid[i+2][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i+2][j]!=grid[i][j]:
                            grid[i+1][j] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i+3][j]!=0 and grid[i+2][j]!=0 and grid[i+1][j]!=0:
                        if grid[i][j]==grid[i+1][j]:
                            grid[i+1][j] = grid[i+1][j]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i+1][j]==grid[i+2][j]:
                            grid[i+2][j] = grid[i+2][j]+grid[i+1][j]
                            grid[i+1][j] = 0
                        elif grid[i+3][j]==grid[i+2][j]:
                            grid[i+3][j] = grid[i+3][j]+grid[i+2][j]
                    elif grid[i+3][j]!=0 and grid[i+2][j]==0 and grid[i+1][j]!=0:
                        if grid[i+1][j]==grid[i][j]:
                            grid[i+2][j] = grid[i+1][j]+grid[i][j]
                            grid[i+1][j] = 0
                            grid[i][j] = 0
                        elif grid[i+3][j]==grid[i+1][j]:
                            grid[i+3][j] = grid[i+3][j]+grid[i+1][j]
                            grid[i+2][j] = grid[i][j]
                            grid[i+1][j] = 0
                            grid[i][j] = 0
                        elif grid[i+1][j]!=grid[i][j] and grid[i+3][j]!=grid[i+1][j]:
                            grid[i+2][j] = grid[i+1][j]
                            grid[i+1][j] = grid[i][j]
                            grid[i][j] = 0
            elif i==1:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i+2][j]==0:
                        if grid[i+1][j]==0:
                            grid[i+2][j] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i+1][j]==grid[i][j]:
                            grid[i+2][j] = grid[i+1][j]+grid[i][j]
                            grid[i+1][j] = 0
                            grid[i][j] = 0
                        elif grid[i+1][j]!=grid[i][j]:
                            grid[i+2][j] = grid[i+1][j]
                            grid[i+1][j] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i+2][j]!=0 and grid[i+1][j]!=0:
                        if grid[i+2][j]==grid[i+1][j]:
                            grid[i+2][j] = grid[i+2][j]+grid[i+1][j]
                            grid[i+1][j] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i+2][j]!=grid[i+1][j]:
                            if grid[i+1][j]==grid[i][j]:
                                grid[i+1][j] = grid[i+1][j]+grid[i][j]
                                grid[i][j] = 0
                            elif grid[i+1][j]!=grid[i][j]:
                                continue
                    elif grid[i+2][j]!=0 and grid[i+1][j]==0:
                        if grid[i+2][j]==grid[i][j]:
                            grid[i+2][j] = grid[i+2][j]+grid[i][j]
                            grid[i][j] = 0
            elif i==2:
                if grid[i][j]==0:
                    continue
                elif grid[i+1][j]!=0:
                    if grid[i][j]==grid[i+1][j]:
                        grid[i+1][j] = grid[i][j]+grid[i+1][j]
                        grid[i][j] = 0
                    elif grid[i][j]!=grid[i+1][j]:
                        continue
                elif grid[i+1][j]==0 and grid[i][j]!=0:
                    grid[i+1][j] = grid[i][j]
                    grid[i][j] = 0
            elif i==3:
                continue    
    
def push_left(grid):
    """merge grid values left"""
    for i in range(4):
        for j in range(4):
            if j==0:
                continue
            elif j==1:
                if grid[i][j]==0:
                    continue
                elif grid[i][j-1]!=0:
                    if grid[i][j]==grid[i][j-1]:
                        grid[i][j-1] = grid[i][j]+grid[i][j-1]
                        grid[i][j] = 0
                    elif grid[i][j]!=grid[i][j-1]:
                        continue
                elif grid[i][j-1]==0:
                    grid[i][j-1] = grid[i][j]
                    grid[i][j] = 0
            elif j==2:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i][j-2]==0:
                        if grid[i][j-1]==0:
                            grid[i][j-2] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j-1]==grid[i][j]:
                            grid[i][j-2] = grid[i][j-1]+grid[i][j]
                            grid[i][j-1] = 0
                            grid[i][j] = 0
                        elif grid[i][j-1]!=grid[i][j]:
                            grid[i][j-2] = grid[i][j-1]
                            grid[i][j-1] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i][j-2]!=0 and grid[i][j-1]!=0:
                        if grid[i][j-2]==grid[i][j-1]:
                            grid[i][j-2] = grid[i][j-2]+grid[i][j-1]
                            grid[i][j-1] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j-2]!=grid[i][j-1]:
                            if grid[i][j-1]==grid[i][j]:
                                grid[i][j-1] = grid[i][j-1]+grid[i][j]
                                grid[i][j] = 0
                            elif grid[i][j-1]!=grid[i][j]:
                                continue
                    elif grid[i][j-2]!=0 and grid[i][j-1]==0:
                        if grid[i][j-2]==grid[i][j]:
                            grid[i][j-2] = grid[i][j-2]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j-2]!=grid[i][j]:
                            grid[i][j-1] = grid[i][j]
                            grid[i][j] = 0
            elif j==3:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i][j-3]==0:
                        if grid[i][j-2]==0:
                            if grid[i][j-1]==0:
                                grid[i][j-3] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i][j-1]!=0 and grid[i][j]!=grid[i][j-1]:
                                grid[i][j-3] = grid[i][j-1]
                                grid[i][j-1] = 0
                                grid[i][j-2] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i][j-1]!=0 and grid[i][j]==grid[i][j-1]:
                                grid[i][j-3] = grid[i][j]+grid[i][j-1]
                                grid[i][j] = 0
                                grid[i][j-1] = 0
                        elif grid[i][j-2]!=0 and grid[i][j-1]==0:
                            if grid[i][j-2]==grid[i][j]:
                                grid[i][j-3] = grid[i][j-2]+grid[i][j]
                                grid[i][j] = 0
                                grid[i][j-2] = 0
                            elif grid[i][j-2]!=grid[i][j]:
                                grid[i][j-3] = grid[i][j-2]
                                grid[i][j-2] = grid[i][j]
                                grid[i][j] = 0
                        elif grid[i][j-2]!=0 and grid[i][j-1]!=0:
                            if grid[i][j-2]==grid[i][j-1]:
                                grid[i][j-3] = grid[i][j-2]+grid[i][j-1]
                                grid[i][j-2] = grid[i][j]
                                grid[i][j] = 0
                                grid[i][j-1] = 0
                            elif grid[i][j-1]==grid[i][j]:
                                grid[i][j-3] = grid[i][j-2]
                                grid[i][j-2] = grid[i][j-1]+grid[i][j]
                                grid[i][j] = 0
                                grid[i][j-1] = 0
                            elif grid[i][j-2]!=grid[i][j-1] and grid[i][j-1]!=grid[i][j]:
                                grid[i][j-3] = grid[i][j-2]
                                grid[i][j-2] = grid[i][j-1]
                                grid[i][j-1] = grid[i][j]
                                grid[i][j] = 0
                    elif grid[i][j-3]!=0 and grid[i][j-2]==0 and grid[i][j-1]==0:
                        if grid[i][j-3]==grid[i][j]:
                            grid[i][j-3] = grid[i][j-3]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j-3]!=grid[i][j]:
                            grid[i][j-2] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i][j-3]!=0 and grid[i][j-2]!=0 and grid[i][j-1]==0:
                        if grid[i][j-2]==grid[i][j]:
                            grid[i][j-2] = grid[i][j-2]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j-2]!=grid[i][j]:
                            grid[i][j-1] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i][j-3]!=0 and grid[i][j-2]!=0 and grid[i][j-1]!=0:
                        if grid[i][j]==grid[i][j-1]:
                            grid[i][j-1] = grid[i][j-1]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j-1]==grid[i][j-2]:
                            grid[i][j-2] = grid[i][j-2]+grid[i][j-1]
                            grid[i][j-1] = 0
                        elif grid[i][j-3]==grid[i][j-2]:
                            grid[i][j-3] = grid[i][j-3]+grid[i][j-2]
                    elif grid[i][j-3]!=0 and grid[i][j-2]==0 and grid[i][j-1]!=0:
                        if grid[i][j-1]==grid[i][j]:
                            grid[i][j-2] = grid[i][j-1]+grid[i][j]
                            grid[i][j-1] = 0
                            grid[i][j] = 0
                        elif grid[i][j-3]==grid[i][j-1]:
                            grid[i][j-3] = grid[i][j-3]+grid[i][j-1]
                            grid[i][j-2] = grid[i][j]
                            grid[i][j-1] = 0
                            grid[i][j] = 0
                        elif grid[i][j-1]!=grid[i][j] and grid[i][j-3]!=grid[i][j-1]:
                            grid[i][j-2] = grid[i][j-1]
                            grid[i][j-1] = grid[i][j]
                            grid[i][j] = 0

def push_right(grid):
    """merge grid values right"""
    for i in range(4):
        for j in range(4):
            if j==0:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i][j+3]==0:
                        if grid[i][j+2]==0:
                            if grid[i][j+1]==0:
                                grid[i][j+3] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i][j+1]!=0 and grid[i][j]!=grid[i][j+1]:
                                grid[i][j+3] = grid[i][j+1]
                                grid[i][j+1] = 0
                                grid[i][j+2] = grid[i][j]
                                grid[i][j] = 0
                            elif grid[i][j+1]!=0 and grid[i][j]==grid[i][j+1]:
                                grid[i][j+3] = grid[i][j]+grid[i][j+1]
                                grid[i][j] = 0
                                grid[i][j+1] = 0
                        elif grid[i][j+2]!=0 and grid[i][j+1]==0:
                            if grid[i][j+2]==grid[i][j]:
                                grid[i][j+3] = grid[i][j+2]+grid[i][j]
                                grid[i][j] = 0
                                grid[i][j+2] = 0
                            elif grid[i][j+2]!=grid[i][j]:
                                grid[i][j+3] = grid[i][j+2]
                                grid[i][j+2] = grid[i][j]
                                grid[i][j] = 0
                        elif grid[i][j+2]!=0 and grid[i][j+1]!=0:
                            if grid[i][j+2]==grid[i][j+1]:
                                grid[i][j+3] = grid[i][j+2]+grid[i][j+1]
                                grid[i][j+2] = grid[i][j]
                                grid[i][j] = 0
                                grid[i][j+1] = 0
                            elif grid[i][j+1]==grid[i][j]:
                                grid[i][j+3] = grid[i][j+2]
                                grid[i][j+2] = grid[i][j+1]+grid[i][j]
                                grid[i][j] = 0
                                grid[i][j+1] = 0
                            elif grid[i][j+2]!=grid[i][j+1] and grid[i][j+1]!=grid[i][j]:
                                grid[i][j+3] = grid[i][j+2]
                                grid[i][j+2] = grid[i][j+1]
                                grid[i][j+1] = grid[i][j]
                                grid[i][j] = 0
                    elif grid[i][j+3]!=0 and grid[i][j+2]==0 and grid[i][j+1]==0:
                        if grid[i][j+3]==grid[i][j]:
                            grid[i][j+3] = grid[i][j+3]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j+3]!=grid[i][j]:
                            grid[i][j+2] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i][j+3]!=0 and grid[i][j+2]!=0 and grid[i][j+1]==0:
                        if grid[i][j+2]==grid[i][j]:
                            grid[i][j+2] = grid[i][j+2]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j+2]!=grid[i][j]:
                            grid[i][j+1] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i][j+3]!=0 and grid[i][j+2]!=0 and grid[i][j+1]!=0:
                        if grid[i][j]==grid[i][j+1]:
                            grid[i][j+1] = grid[i][j+1]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j+1]==grid[i][j+2]:
                            grid[i][j+2] = grid[i][j+2]+grid[i][j+1]
                            grid[i][j+1] = 0
                        elif grid[i][j+3]==grid[i][j+2]:
                            grid[i][j+3] = grid[i][j+3]+grid[i][j+2]
                    elif grid[i][j+3]!=0 and grid[i][j+2]==0 and grid[i][j+1]!=0:
                        if grid[i][j+1]==grid[i][j]:
                            grid[i][j+2] = grid[i][j+1]+grid[i][j]
                            grid[i][j+1] = 0
                            grid[i][j] = 0
                        elif grid[i][j+3]==grid[i][j+1]:
                            grid[i][j+3] = grid[i][j+3]+grid[i][j+1]
                            grid[i][j+2] = grid[i][j]
                            grid[i][j+1] = 0
                            grid[i][j] = 0
                        elif grid[i][j+1]!=grid[i][j] and grid[i][j+3]!=grid[i][j+1]:
                            grid[i][j+2] = grid[i][j+1]
                            grid[i][j+1] = grid[i][j]
                            grid[i][j] = 0
            elif j==1:
                if grid[i][j]==0:
                    continue
                elif grid[i][j]!=0:
                    if grid[i][j+2]==0:
                        if grid[i][j+1]==0:
                            grid[i][j+2] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j+1]==grid[i][j]:
                            grid[i][j+2] = grid[i][j+1]+grid[i][j]
                            grid[i][j+1] = 0
                            grid[i][j] = 0
                        elif grid[i][j+1]!=grid[i][j]:
                            grid[i][j+2] = grid[i][j+1]
                            grid[i][j+1] = grid[i][j]
                            grid[i][j] = 0
                    elif grid[i][j+2]!=0 and grid[i][j+1]!=0:
                        if grid[i][j+2]==grid[i][j+1]:
                            grid[i][j+2] = grid[i][j+2]+grid[i][j+1]
                            grid[i][j+1] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j+2]!=grid[i][j+1]:
                            if grid[i][j+1]==grid[i][j]:
                                grid[i][j+1] = grid[i][j+1]+grid[i][j]
                                grid[i][j] = 0
                            elif grid[i][j+1]!=grid[i][j]:
                                continue
                    elif grid[i][j+2]!=0 and grid[i][j+1]==0:
                        if grid[i][j+2]==grid[i][j]:
                            grid[i][j+2] = grid[i][j+2]+grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][j+2]!=grid[i][j]:
                            grid[i][j+1] = grid[i][j]
                            grid[i][j] = 0
            elif j==2:
                if grid[i][j]==0:
                    continue
                elif grid[i][j+1]!=0:
                    if grid[i][j]==grid[i][j+1]:
                        grid[i][j+1] = grid[i][j]+grid[i][j+1]
                        grid[i][j] = 0
                    elif grid[i][j]!=grid[i][j+1]:
                        continue
                elif grid[i][j+1]==0:
                    grid[i][j+1] = grid[i][j]
                    grid[i][j] = 0
            elif j==3:
                continue