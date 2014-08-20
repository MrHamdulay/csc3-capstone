# program to adjust text
# Matthew Bandama
# BNDTAT003
# 13-May-2014

def get_file(filename):
    
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    
    sentences = dict()
    line_number = 0

    for j in lines:
        
        sentences[line_number] = j.split(' ')
        line_number +=1
    
    return(sentences)




def new_file(filename,d,length):
    l = length
    
    f = open(filename,'w')
    
    for i in d:
        
        for j in range(len(d[i])):
            
            
            
                
            if l >= len(d[i][j])+1:
                print(d[i][j],end = ' ',file = f)
                l = l - (len(d[i][j])+1)
            else:
                print('',file = f)
                print(d[i][j],end=' ',file = f)
                l = length
                l = l - (len(d[i][j])+1)
    f.close()




def main():
    
    print('Enter the input filename:')
    filename = input()
    
    
    print('Enter the output filename:')
    out_filename = input()
    
    
    print('Enter the line width:')
    width = eval(input())
    
    
    sentences = get_file(filename)
    
    new_file(out_filename,sentences,width)
    

if __name__=='__main__':
    main()






    
    
        
