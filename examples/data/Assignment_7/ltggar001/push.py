import util

def push_up (grid):
    """merge grid values upwards"""
    for q in range(4):
        a=grid[0][q]
        b=grid[1][q]
        c=grid[2][q]
        d=grid[3][q]
        z=0
        while a == 0:
            a=b
            b=c
            c=d
            d=0
            z+=1
            if z == 5:
                break
        x=0
        while b == 0:
            b=c
            c=d
            d=0
            x+=1
            if x == 5:
                break    
        v=0
        while c == 0:
            c=d
            d=0
            v+=1
            if v == 5:
                break  
        if a==b:
            a=a*2
            b=c
            c=d
            d=0
        if b==c:
            b=b*2
            c=d
            d=0
        if c==d:
            c=c*2
            d=0

        grid[0][q]=a
        grid[1][q]=b
        grid[2][q]=c
        grid[3][q]=d
        m=[a,b,c,d]
        grid.append(m)
        
def push_down (grid):
    """merge grid values downwards"""
    for q in range(4):
        a=grid[3][q]
        b=grid[2][q]
        c=grid[1][q]
        d=grid[0][q]
        z=0
        while a == 0:
            a=b
            b=c
            c=d
            d=0
            z+=1
            if z == 5:
                break
        x=0
        while b == 0:
            b=c
            c=d
            d=0
            x+=1
            if x == 5:
                break    
        v=0
        while c == 0:
            c=d
            d=0
            v+=1
            if v == 5:
                break  
        if a==b:
            a=a*2
            b=c
            c=d
            d=0
        if b==c:
            b=b*2
            c=d
            d=0
        if c==d:
            c=c*2
            d=0

        grid[3][q]=a
        grid[2][q]=b
        grid[1][q]=c
        grid[0][q]=d
        m=[a,b,c,d]
        grid.append(m)

def push_left (grid):
    """merge grid values left"""
    for q in range(4):
        a=grid[q][0]
        b=grid[q][1]
        c=grid[q][2]
        d=grid[q][3]
        z=0
        while a == 0:
            a=b
            b=c
            c=d
            d=0
            z+=1
            if z == 5:
                break
        x=0
        while b == 0:
            b=c
            c=d
            d=0
            x+=1
            if x == 5:
                break    
        v=0
        while c == 0:
            c=d
            d=0
            v+=1
            if v == 5:
                break  
        if a==b:
            a=a*2
            b=c
            c=d
            d=0
        if b==c:
            b=b*2
            c=d
            d=0
        if c==d:
            c=c*2
            d=0

        grid[q][0]=a
        grid[q][1]=b
        grid[q][2]=c
        grid[q][3]=d
        m=[a,b,c,d]
        grid.append(m)

def push_right (grid):
    """merge grid values right"""
    for q in range(4):
        a=grid[q][3]
        b=grid[q][2]
        c=grid[q][1]
        d=grid[q][0]
        z=0
        while a == 0:
            a=b
            b=c
            c=d
            d=0
            z+=1
            if z == 5:
                break
        x=0
        while b == 0:
            b=c
            c=d
            d=0
            x+=1
            if x == 5:
                break    
        v=0
        while c == 0:
            c=d
            d=0
            v+=1
            if v == 5:
                break  
        if a==b:
            a=a*2
            b=c
            c=d
            d=0
        if b==c:
            b=b*2
            c=d
            d=0
        if c==d:
            c=c*2
            d=0

        grid[q][3]=a
        grid[q][2]=b
        grid[q][1]=c
        grid[q][0]=d
        m=[a,b,c,d]
        grid.append(m)