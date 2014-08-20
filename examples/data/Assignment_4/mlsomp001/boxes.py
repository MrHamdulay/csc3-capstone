
# Name: OMPHEMETSE
# Student no: MLSOMP001
# DATE: 04 APRIL 2014
# ASSIGNMENT RATING: TORTURE

def print_square():
    print("*****")
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')

def print_rectangle(width,height):
    print('*'*width)
    spacing=width-2
    for i in range(height-2):
        print('*'+' '*spacing+'*')
    print('*'*width)

def get_rectangle(width,height):
    boxes_string='*'*width+'\n'
    for i in range(height-2):
        boxes_string+='*'
        for i in range(width-2):
            boxes_string+=' '
        boxes_string+='*\n'
    boxes_string+='*'*width

    return boxes_string


