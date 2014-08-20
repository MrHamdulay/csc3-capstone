import random
R = 2
C = 3
mx = int(random.randint(0,C-1))
my = int(random.randint(0,R-1) )
xval = []
yval =[]
cord = [xval,yval]
for y in range(R):
    cord[1].append(0)
for x in range(C):
    cord[0].append(0)

cord[0+1][0]+=1



for y in range(R):
    for x in range(C):
        if mx == x and my ==y:
            print("*", end  ="")
        else:
            print(cord[x-1][y-1],end = "")
        
    print()


            

    