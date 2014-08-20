"""program to reformat to specific width
Paul Truter
16 May 2014"""

input_file = input('Enter the input filename: \n')
output_file = input('Enter the output filename: \n')
width = eval(input('Enter the line width: \n'))


f = open(input_file, "r")
r = f.read()
f.close()

output=[]

w = width
def reformat(text,w):
    while text:
        #if text if over width
        if len(text) <= w: 
            output.append(text[:len(text)])
            text = ''
            return output
        else:
            #from start of text to width(cut off rest)
            for j in text[0:w + 1]: 
                if text[w] == ' ':
                    output.append(text[:w])
                    return reformat(text[w+1:],w)
                else: 
                    return reformat(text,w-1)

x = reformat(r,w)

#write reformatted text to new file
f = open (output_file, "w")
for i in x:
    print(i)
    print (i, file=f, end='')
f.close () 

    