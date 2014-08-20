def tri():
    height=eval(input("Enter the height of the triangle:" '\n'))
    weight=(2*height)-1
    character="*"
    space=weight//2
    for i in range(0,weight,2):
        print(' '*space,end='')
        print(character*(i+1))
        space=space-1
        
tri()