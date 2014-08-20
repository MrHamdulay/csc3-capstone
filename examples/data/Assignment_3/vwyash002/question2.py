#triangle

height= eval(input("Enter the height of the triangle: \n"))
spaces = height-1
numStars = 1
result = ""
for i in range(height,0,-1): 
    result = result+(spaces*' ')+numStars*'*'+(spaces*' ')+'\n'
    spaces = spaces -1
    numStars = numStars +2
print(result)