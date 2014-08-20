"""Removing repeated words
Richard Marais
14/05/02"""

def norepeats():   #funtion
    print("Enter strings (end with DONE):")      #string to prompt input  
    j = 0
    lista = []
    while j != 'DONE':            #while loop with done sentinel to keep taking in input
        j = input('')
        while j != 'DONE' and j not in lista:
            lista.append(j)                    #only append things that arent in the list
    print("\nUnique list:")   
    for i in lista:
        print(i)               #print the list
        
        
norepeats()