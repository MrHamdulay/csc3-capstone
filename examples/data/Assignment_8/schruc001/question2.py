'''Recursive Program to count repeated pairs of characters in strings
Ruchaan Schmidt
May 2014'''

string = input('Enter a message:\n')

# paircount
pc = 0

def count (string):
  
# keep proper total
    global pc
    
    #string = string.lower()
    if len(string) == 0:
        print ('Number of pairs: 0')

    elif len(string) == 1:
        print ('Number of pairs:', pc)

    elif len(string) == 2:
        if string[0]==string[1]:
            pc+=1
            print ('Number of pairs:', pc)
        else:
            print('Number of pairs:', pc)

    else:
        if string[0]==string[1]:
            pc+=1
            temp = string[1:len(string)-1]
            if string[0]==string[1]:
                temp = string[2:len(string)]
            else:
                temp = string[1:len(string)]
            count (temp)
                
        else:
            temp = string[1:len(string)]
            count (temp)
            #print (temp)
    
    
count(string)