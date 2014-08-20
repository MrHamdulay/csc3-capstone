# Right-aligned list
# Irfan Habib
# 2014/04/23

def main():
    list1 = []
    max = 0
    print('Enter strings (end with DONE):\n')
    i = input()
    while i != 'DONE':
        list1.append(i)
        
        if max < len(i):
            max = len(i)
        i = input()   

    print('Right-aligned list:')        
    for k in range(len(list1)):
        print((max-len(list1[k]))*' '+list1[k])
   
     

main()
    
    
    
    