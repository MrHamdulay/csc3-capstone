def reformat(filename,output,width):
    f=open(filename,'r')
    lines= f.readlines()
    f.close()
    
    len_words=0
    form= ''
    for line in lines:
        words= line[:-1].split(' ')
        for word in words:
            len_words+= len(word)
            if len_words> width:
                form+="\n"+word+' '
                len_words= len(word)+1
            elif len_words== width:
                form+=word+'\n'
                len_words=0             
            else:
                form+=word+' '
                len_words+=1
                
    f=open(output,'w')
    f.write(form)
    f.close()

filename= input('Enter the input filename:\n')
output=input('Enter the output filename:\n')
width= eval(input('Enter the line width:\n'))
reformat(filename,output,width)