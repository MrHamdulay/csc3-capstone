#Thembekile Dubazana
#DBZPHI002
#Assignment 4: Rectangles

def print_square():
    for i in range(1,6):
        if i==1 or i==5:
            print('*'*5,sep="")
        else:
            print('* ',"",'*')
            
def print_rectangle(width,height):
    newheight=height+1
    for i in range(1,newheight):
        if i==1 or i==height:
            print('*'*width,sep="")
        else:
            space=width-2
            print('*',' '*space,'*',sep="")
            
def get_rectangle(width,height):
    width=int(width)
    height=int(height)
    r=height-2
    inner=" "*(width-2)
    top='*'*width
    mid='*'+inner+'*'+'\n'
    mid=mid*r
    box=top+'\n'+mid+top
    return box





            