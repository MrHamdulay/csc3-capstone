#GLMSUM001
#Sumayah Goolam Rassool
#16 April 2014

#-------------------------------Maths class is imported to make use of trig functions----------------------------

import math 

#------------------------------Allows user to enter a function of the graph to be drawn--------------------------

function=(input("Enter a function f(x):\n"))

#-----------------------------allows for a graphing grid to be created containing x and y values-----------------

for y in range(-10,11):
    
    line=''
    block=''

#----------------------------Allows for x and y axes to run from negative 10 to positive 10----------------------

    y*=-1
    for x in range(-10,11):
       
        if y==0 and x==0 : 
            block='+'#------------------------------------marks the origin of cartesian plane
            
        elif x==0 : 
            block='|'#------------------------------------draws the y-axis
            
        elif y==0 : 
            block='-'#------------------------------------draws the x-axis
            
        else: 
            block=' '
    
        f = function.replace('x','('+str(x)+')')
        if round(eval(f)) == y: 
            block='o'#-------------------------------------draws graph using 'o'
        
        line+=block#---------------------------------------rest of the line is made up of empty spaces
        block=''
    print(line)
        
        
            

        


      
                        
