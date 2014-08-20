"""CSC1015F Assignment 7 Question 1
Xola Matlanyane MTLXOL002
2 May 2014"""

def main(): #create main program(me)
    somelist = [] #create some list (by adding to the list)
    print ("Enter strings (end with DONE):")
    
    while True:
        resp = input('')
        
        if resp in somelist:
            continue   #recording duplication of response of strings
        
        elif resp == 'DONE':
            break     #stop 'requesting' values when DONE is entered
        
        else:
            somelist.append(resp) #append list with response
            
    print("\nUnique list:")    
    for i in somelist:
        print(i)
            
if __name__ == '__main__': main()