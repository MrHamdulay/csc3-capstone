#Kovlin Perumal
#21/04/14
#Question4 - Histogram

marks = list(map(int,input("Enter a space-separated list of marks:\n").split())) #Populate marks array
bars = ['', '', '', '', ''] #Assign empty strings to bars array

for i in marks :
    if(i < 50):
        bars[0] += ("X")
    elif(50 <= i < 60):
        bars[1] +=("X")
    elif(60 <= i < 70):
        bars[2]+=("X")
    elif(70 <= i < 75):
        bars[3]+=("X")
    elif(75 <= i):
        bars[4]+= ("X") #populate bars with Xs  
    
print("1 |",bars[4],"\n2+|",bars[3],"\n2-|",bars[2],"\n3 |",bars[1],"\nF |",bars[0], sep = '')#output