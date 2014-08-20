#Yaseen Sayed Ismail
#SYDYAS003
#11/05/2014
#Program to reformat a text file so that all lines are at most a given length

filename = input("Enter the input filename:\n")#Receive the input file name from user
f = open(filename,"r")#Opens input file to be read from

output = input("Enter the output filename:\n")#Receive the output file from user
k = open(output,"w")#Opens output file to be written to

text=f.read()#Stores all the text from the input file in a string

posit=0#Define variable to store index of space later on
start=-1#Define variable start

width = eval(input("Enter the line width:\n"))#Receive width from user


for i in range(len(text)):#Loops through text from input file
    
    #Checks if current position is the last position in the string, if so, writes to output file all the characters from one position after start till current index, excluding any '\n'.
    if(i==len(text)-1):
            x=[]
            x.append(text[start+1])
            for j in range(start+2,i):
                if(text[j]!='\n'):
                    x.append(text[j])
                else:
                    x.append(" ")
            x.append(text[i])      
            for j in x:
                print(j,end='',file=k)

    #Checks line spacing for the case of a blank line being left open, if so, leaves a blank line and then writes all the characters from one position after start to current position, excluding any '\n'.          
    elif(text[i]=="\n" and text[i+1]=="\n"):
        x=[]
        x.append(text[start+1])
        for j in range(start+2,i):
            if(text[j]!='\n'):
                x.append(text[j])
            else:
                x.append(" ")
        x.append(text[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        start=i+1#Sets start to the following index, in order to leave out the '\n'     
    
    #Checks if the number of characters since the last writing is equal to the specified width and if the next character is a space, if so, writes all the characters from the position after start to the current position. Removes any '\n'
    elif(i==start+width and text[i+1]==" "):
        x=[]
        x.append(text[start+1])
        for j in range(start+2,i):
            if(text[j]!='\n'):
                x.append(text[j])
            else:
                x.append(" ")
        x.append(text[i])
        for j in x:
            print(j,end='',file=k)
        print("",file=k)        
        
        start=i+1#Sets start to the next position in order to leave out the space
    
    #Checks if the number of characters since the last writing is equal to the specified width and if the next character is not a space, if so, writes all the characters from the position after start to the postion of the last space or the last '\n'. Removes any '\n'.
    elif(i==start+width and text[i+1]!=" "):  
        #Loop to determine position of last space or last '\n'
        for j in range(i,start,-1):
            if(text[j]==" " or text[j]=="\n"):
                posit=j
                break
        x=[]
        x.append(text[start+1])
        for j in range(start+2,posit-1):
            if(text[j]!='\n'):
                x.append(text[j])
            else:
                x.append(" ")
        x.append(text[posit-1])        
        for j in x:
            print(j,end='',file=k)
        print("",file=k)
        start=posit#Sets start to postion of last space or last '\n'

#Closes files
f.close()
k.close()