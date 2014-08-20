'''program to count votes in election
Thabiso Beau
23 April 2014
Assignment 6: #question3'''

def main(): 
    #eerste deel - vra vir mens om lys te voltooi 
    enter=[]
    print('Independent Electoral Commission')
    print('-'*len('Independent Electoral Commission'))
    fruit=input('Enter the names of parties (terminated by DONE): \n')
    #begin die lys
    while fruit!='DONE': #DONE tree op as die sentinel
        enter.append(fruit) #die input word daar ingesit
        fruit=input('') #leeg snaar
    #tweede deel - tel die stemme
    print()
    print('Vote counts:')
    tel={} #maak funksie wat stemme gaan tel
    for i in enter:
        if i not in tel: #as naam nie gevind nie, sit in woordeboek
            tel[i] = 1
        else:
            tel[i] +=1
    
    for i in sorted(tel.keys()): #wys die spasies in die program
        print(i.ljust(10), '-', (tel[i]))
    
main()

#enter=['']
    #for i in range(len(fruit)):
        #if not fruit[i] in enter:
            #enter.append(fruit)
        #else:
            #pass  
    #for i in range(len(enter)):
        #fruit.count(enter(i))