# Author : Rayaan Fakier FKRRAY001
# Date : 11 - 05 - 2014
# question2.py

def formatter(infile, outfile, width):
    inf = open(infile)
    inflines = inf.readlines()
    inf.close()
    
    act_inflines = []
    # Creates array without '\n'
    for index in range(len(inflines)-1):
        act_inflines.append(inflines[index][:len(inflines[index])-1])
    act_inflines.append(inflines[len(inflines)-1])
    
    print(act_inflines)
    print("end \n")
    # Creates single string of all lines
    fin_inflines = []
    fin_inflines.append(act_inflines[0])
    if len(act_inflines) > 1:
        for index2 in range(1,len(act_inflines)):
            fin_inflines[0] += act_inflines[index2]
        
    #print(fin_inflines)
    #print("end \n")
    
    
    
    outf = open(outfile, 'w')
    for j in range(len(fin_inflines)):
        num = 0
        add_words = ""
        if len(fin_inflines) > width:
            print("YES")
            for i in range(width, len(j)):
                add_words += j[i]
            print(add_words)
        #for k in range(len(j)):
            #while (k%width != 0):
                #print(j[k])
            
            #if num == 0:
                #print(j[k], end='')
                #num+=1
            #elif (num%width == 0):
                #if j[k+1].isalpha():
                    #print(end='')
                    #r = 0
                    #while j[k-r].isalpha():
                        #print(j[k-r],end='')
                        #r+=1
                    #num += 1
                #else:
                    #print()
                    #print(j[k],end='')
                    #num+=1
            #else:
                #print(j[k],end='')
                #num += 1
    outf.close()
    
    
    outf2 = open(outfile)
    outf2.close()   
    
    
    
if __name__ == '__main__':
    #infile = input("Enter the input filename:\n")
    #outfile = input("Enter the output filename:\n")
    #width = int(input("Enter the line width:\n"))
    #formatter(infile, outfile, width)
    formatter('input.txt', 'mo.txt', 40)