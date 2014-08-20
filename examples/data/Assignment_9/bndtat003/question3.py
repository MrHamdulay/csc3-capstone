# check if sodoku is done
# Matthew Bandama
# BNDTAT003
# 13-May-2014


def get_file(filename):
    f = open(filename,'r')
    info = f.readlines()
    f.close()
    
    
    for k in range(len(info)):
        info[k] = info[k][:-1]
    
    final = []
    
    for i in range(len(info)):
        first = []
        for j in range(len(info[i])):

            first.append(eval(info[i][j]))
        final.append(first)
    return(final)



def create_sod():
    sod = []
    n_row = input()
    
    while n_row:
         sod.append(n_row)
         n_row = input()
    sodoku = []
    
    for i in range(len(sod)):
         temp_store = []
	 
         for j in range(len(sod[i])):
             temp_store.append(eval(sod[i][j]))
         sodoku.append(temp_store)
    return(sodoku)



def check_row(l):
    
    for i in range(len(l)):
        
        for j in range(1,10):
            
            if j not in l[i]:
                return(False)
    
    return(True)


def check_col(l):
    
    new_l = []

    for i in range(len(l)):
        
        temp_l = []
        
        for j in range(len(l[i])):
            
            temp_l.append(l[j][i])
        
        new_l.append(temp_l)
    
    return(check_row(new_l))


def check_box(l):
    
    opt_list = [1,2,3,4,5,6,7,8,9]
    condition = True
    for z in [0,3,6] : # next process shoud happen three times

         for j in range(9):

             for k in range(z,z+3):

                 if len(opt_list) == 0:
                     opt_list = [1,2,3,4,5,6,7,8,9]

                 if l[j][k] in opt_list:
                     index = opt_list.index(l[j][k])
                     del opt_list[index]

                 else:
                     condition = False
    return(condition)


def main():
    
    
    #filename = input()
    #l = create_sod()
    sod = []
    n_row = input()
    
    while n_row:
         sod.append(n_row)
         n_row = input()
    sodoku = []
    
    for i in range(len(sod)):
         temp_store = []
	 
         for j in range(len(sod[i])):
             temp_store.append(eval(sod[i][j]))
         sodoku.append(temp_store)
    
    a = check_row(sodoku)
    b = check_col(sodoku)
    c = check_box(sodoku)
    
    if a == True and b == True and c == True:
         print('Sudoku grid is valid')
    else:
         print('Sudoku grid is not valid')

if __name__=='__main__':
     main()
     


