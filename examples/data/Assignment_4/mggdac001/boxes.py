def print_square ():
    size = 5
    star =size*"*"
    for x in range(1): #This is for print the top part of the box
        print(star)
    for y in range(size-2): #This is for printing the middle part of the box
        print(str(star)[:1] + " "*(size-2) + str(star)[-1]) #The first part says slice the box from the biginning to 1, and second part says add spaces and multiply them by the input value minus
    for z in range(1): #This is the same as the first comment
        print(star)
        
def print_rectangle (width, height):
    w = width*"*"
    h = height*"*"
    for a in range(1):
        print(w)
    for b in range(height-2):
        print(str(h)[1] + " "*(width-2) + str(h)[-1] )
    for c in range(1):
        print(w)
        
def get_rectangle (width, height):
    rect=''
    for i in range(1,height+1):
        if i==1 or i==height:
            rect+= '*'*width +'\n'
        else: rect+= '*'+' '*(width-2)+'*' + '\n'
    return rect    