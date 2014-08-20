'''program to create a new file with formatted text
Luke Naude
12 May 2014'''

#get the input file
original_filename=input('Enter the input filename:\n')
final_filename=input('Enter the output filename:\n') #get name for output file
line_length=eval(input('Enter the line width:\n'))
original_file=open(original_filename, 'r')#open the file
lines=original_file.read()#assign contents to list

original_file.close()#close the file to avoid error


'''remove '\n' from lines'''
lines=lines.split(' ')#split list into many
repeat =2
#while repeat !=0:
for n in range(0,len(lines)):#check each beginning and end of item for '\n'
    if lines[n][0:1]=='\n':
        lines[n]=lines[n][1:len(lines[n])]#if beginning is '\n' slice it off
    if lines[n][len(lines[n])-1:len(lines[n])]=='\n':
        lines[n]=lines[n][0:len(lines[n])-1]#if end is '\n' slice it off
repeat-=1
'''add a space to the end of each item in lines'''
for i in range(len(lines)-1):
    lines[i]=lines[i]+' '

string_length=0
newList=[]
def wrap_formatting(n):
    global lines
    global string_length
    global newList
    #if n<len(lines):
    if string_length<line_length and n<len(lines):
        string_length+=len(lines[n])
        return wrap_formatting(n+1)
    if string_length==line_length:
        string_length=0
        newList.append(lines[0:n])
        lines=lines[n:]
        n=0
        return wrap_formatting(n)
    if string_length>line_length:
        string_length=0
        newList.append(lines[0:n-1])
        lines=lines[n-1:]
        n=0
        return wrap_formatting(n)
    if n == len(lines): #catch the last word in the lines list and add it to newList
        newList.append(lines)
        return ''
    
wrap_formatting(0)           

newList = ["".join(i) for i in newList]

#turn newList into string


file=open(final_filename, 'w')
for i in newList: 
    print(i,file=file)
file.close()
