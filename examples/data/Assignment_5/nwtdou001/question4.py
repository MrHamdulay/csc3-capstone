import math
f = input('Enter a function f(x):\n')
g = ''
for y in range(10,-11,-1):
    for x in range(-10,11):
        if y-0.5<=eval(f)<y+0.5:
            g+='o'
        else:
            if x==0:
                if y==0:
                    g+='+'
                else: g+='|'
            elif y==0:
                g+='-'
            else:
                g+=' '
    g+='\n'
print(g)