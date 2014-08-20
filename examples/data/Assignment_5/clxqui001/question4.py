"""this function creates a text based graph from a function a user inputs using charaters such as +,-,o
quincy cele 
16 april 2014"""
#import math to allow this program to use functions such as sinX etc
import math 
function=(input("Enter a function f(x):\n"))
#create a nest for loop to create a grid graph with a y and x value
for y in range(-10,11):
    line=''
    block=''
    # by multliplying our y value by negative one, it allows our y value on the cartesian plane to run from positive
    #ten to negative ten
    y*=-1
    for x in range(-10,11):
        #make the centre of the cartesian pane equal to "+"
        if y==0 and x==0 : block='+'
        elif x==0 : block='|'
        elif y==0 : block='-'
        else: 
            block=' '
    
        f = function.replace('x','('+str(x)+')')
        if round(eval(f)) == y: block='o'
        
        line+=block
        block=''
    print(line)
        
        
            

        


      
                        
