#Thea Sitek, STKTHE002
#16.05.2014
#Shortening lines

#input
file = input('Enter the input filename: \n')
outp = input('Enter the output filename: \n')
w = eval(input('Enter the line width: \n'))

#read file
f = open(file, "r")
t = f.read()
f.close()

#remove linechanges
t = t.replace ("\n\n", '@')
t = t.replace ("\n", ' ')
t = t.replace ('@', "\n\n")
          

#create output array
output = []


interval = w   #save the width value as a constant
def lines(text,width):
    while text: #while not through entire text
        if len(text) <= width: #if can fit rest of text into one line
            output.append(text[:len(text)])
            text = ''
            return output #done
        else:
            for j in text[0:width + 1]: #from first element to the width interval
                if text[width] == ' ':
                    output.append(text[:width])
                    return lines(text[width+1:],interval) #run again with rest of text
                else: 
                    return lines(text,width-1) #try with one less element


#call function
final = lines(t,w)

#empty output file
e = open (outp, "w")
print ("", file=e, end='')
e.close () 

#read into output file
for k in final:
    print(k)
    e = open (outp, "a")
    print (k, file=e)
    e.close () 
    