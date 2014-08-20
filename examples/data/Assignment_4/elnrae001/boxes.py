'''Hollow box drawer
Author:Raees Eland
31 March 2014'''

'''prints a 5x5 square'''
def print_square():
    print('*'*5)
    for i in range(3):
        box='{0}{1:>4}'
        print(box.format('*','*'))
    print('*'*5)
    
'''prints a square of given width and height'''
def print_rectangle(width,height):
    print('*'*width)
    for i in range(height-2):
        print('*'+' '*(width-2)+'*')
    print('*'*width)
    
'''returns a square of given width and height'''     
def get_rectangle(width,height):
    box=''
    box+='*'*width+'\n'
    for i in range(height-2):
        box+='*'+' '*(width-2)+'*'+'\n'
    box+='*'*width+'\n' 
    return box



    


