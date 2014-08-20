

def print_square():
    print( '*'*5,'\n','*   *\n'*3,'*'*5,sep='')
#print(print_square()) 

#def middlepiece(w,h):
    #for i in range(1,w-1):
        #print('*',' '*(h-2),'*')
def print_rectangle (width, height):
    print('*'*width)
    for i in range(1,height-1):
        print('*',' '*(width-2),'*', sep="")    
    print('*'*width)





def get_rectangle (width, height):
    output='*'*width
    for i in range(1,height-1):
        output+='\n*'+' '*(width-2)+'*'    
    output+='\n'+'*'*width
    
    return output
#ans = input('Choose test:\n')
#if ans[0:1]=="a":
    #print(square())
#elif ans[0:1]=="b":
    #print('calling function',print_rectangle (eval(ans[2:3]), eval(ans[4:5])),'called function')
#elif ans[0:1]=="c":
    #print('calling function','called function', get_rectangle(eval(ans[2:3]), eval(ans[4:5])))    