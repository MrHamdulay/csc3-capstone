'''Irfan Habib
Unique list program
2014/05/01'''

def main():
    i = input('Enter strings (end with DONE):\n')
    k = 0
    list1= []
    while i !='DONE':
        if i not in list1:
            list1.append(i)
            k += 1
            i = input()
        else: i = input()
    print('\nUnique list:')    
    for j in range(k):
        print(list1[j])
main()
        
        