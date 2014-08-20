height=eval(input("Enter the height of the triangle: \n"))
a=1
b=height

for i in range(height):
    print((' '*(b-1)),('*'*a),sep='')
    a+=2
    b-=1
    
