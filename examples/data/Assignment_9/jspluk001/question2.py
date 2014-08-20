'''Luke Joseph
2014-05-13
Question 2 of assignment 9'''

import textwrap

def main():
    z=""
    f=input("Enter the input filename:\n")
    p=[]
    f=open(f,"r")
    p=f.readlines()
    f.close
    g=input("Enter the output filename:\n")
    f=open(g,"w")
    h=eval(input("Enter the line width:\n"))
    #p=[]
    d=""
    aap=""
    
        
    for i in range(len(p)): #Loop checking for the end of a paragraph
        if p[i]=="\n":
            p[i]="$"
    #print(p)
    new_list  = []

    for i in range(len(p)):# loop appending each paragraph as a string to a list
        z=""
        if p[i]!="$":
            z+=p[i]
            aap+=z
        else:
            new_list.append(z)
            new_list.append("$")
            z = ""
    new_list.append(aap)
            
    #print(new_list)
    for i in range(len(new_list)):
        b=textwrap.wrap(new_list[i],width=h) # Wrapping lines to specified width
        #if b == "$":
         #   for j in range(len(b))
          #  print(file =f)
        #else:
        for i in range(len(b)): # Overwriting file with new text
            if b[i] == "$":
                print(file =f)
            else:
                print(b[i],file = f)
    f.close()
   
main()