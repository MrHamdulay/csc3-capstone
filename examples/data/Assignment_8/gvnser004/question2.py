"""
Serayen Govender 
check paired letters
"""

c=0
#counter
def count_func(stri):

    global c

    if stri=='':

        return c
    #recursion finished: Gone through all characters of word

    else:

        if(len(stri)>1):
            if(stri[0]==stri[1]):
                c+=1
                
            #find repeted words


            return count_func(stri[2:len(stri)])
        #recuresion step: send modified word to function again

        else:

            return count_func(stri[1:len(stri)])
        #recuresion step: send modified word to function again


inp_num=input("Enter a message:\n")         

print("Number of pairs:",count_func(inp_num))