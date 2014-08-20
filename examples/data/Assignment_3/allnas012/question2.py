
t=eval(input("Enter the height of the triangle:\n"))
last=(t*2)-1
for i in range(1,last+1,2):
    line = '*' * i 
    line = line.center(last, ' ') 
    print(line) 
        
