x = input("Enter a message:\n")
def check(x,count):
    #count = 0
    length = len(x)
    if 1 == len(x):
        print("Number of pairs:",round(count),sep=' ')
    elif 2 ==len(x) and x[0] == x[1]:
        print("Number of pairs:",round(count+1),sep=' ')    
    elif x[0] == x[1]:
        y = 2
        step = x[y:length]
        count+=1.
        check(step,count)
        return

    else:
        z = 1
        step2 = x[z:length]
        check(step2,count)
check(x,0)
        

