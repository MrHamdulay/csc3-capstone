"""Progra to align width
Sbonelo Mntungwa
16 May 2014"""
#Assigning variables
input_file = input("Enter the input filename:\n")
output_file = input("Enter the output filename:\n")
x = eval(input("Enter the line width:\n"))
#opening file
f = open(input_file,'r')
file = f.readlines()
f.close()
#creating lists
list1 = []
list2 = []
#Breaking string into character by character
for i in file:
    list2.append(i)
    for j in i:
        list1.append(j)
#Creating final string        
new_text = ''
#Defining function redo
def redo(list1,new_text):
    #Writing on output text file if function is done recurring
    if len(list1) < x:
        list1=''.join(list1)
        new_text+=list1
        g = open(output_file,'w')
        print(new_text,file = g)
        g.close()
    #Creating temporal variables    
    else:
        count = 0
        temp1 = []
        temp2 = ''
        #adding characters to new_text variable
        while count<x:
            new_text += list1[count]
            count+=1
        #putting characters in a list form 
        for i in new_text:
            temp1.append(i)
        #taking out characters which are seperated   
        while temp1[-1] != ' ':
            temp2+=temp1.pop(-1)
        #swapping list    
        temp2 = temp2[::-1]
        new_text = ''.join(temp1)+'\n'+temp2
        #repeating function redo
        return redo(list1[x:],new_text)   
    
redo(list1,new_text)       