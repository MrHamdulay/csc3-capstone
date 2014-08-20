# Drawer
# Irfan Habib
# 2 April 2014

def print_square():
    for i in range(5):
        if i == 0 or i == 4:
            print(5*'*')
        else: print('*   *')

def print_rectangle(w,h):
    for i in range(h):
        if i == 0 or i==h-1:
            print(w*'*')
        else:
            print('*','*',sep=(w-2)*' ')
            
def get_rectangle(w,h):
    rec = ''
    for i in range(h):
        if i == 0 or i==h-1:
            rec += (w*'*')+'\n'
        else:
            rec +='*'+((w-2)*' ')+'*' + '\n'
    return rec        
    

            