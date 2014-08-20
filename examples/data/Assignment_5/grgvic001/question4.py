import math
def main():
    functionx = input('Enter a function f(x):\n')
    for i in range(10,-11,-1):
        for q in range(-10,11,1):
            if functionx.find('x') == -1:
                if round(eval(functionx)) == i:    
                    print('o',end='')
                elif q == 0 and i == 0:
                    print('+',end='')
                elif q == 0:
                    print('|',end='')
                elif i == 0:
                    print('-',end='')
                else: print(' ',end='')                
                continue
            if round(eval(functionx[:functionx.find('x')] + '('+ str(q) + ')' + functionx[functionx.find('x')+1:])) == i:
                print('o',end='')
            elif q == 0 and i == 0:
                print('+',end='')
            elif q == 0:
                print('|',end='')
            elif i == 0:
                print('-',end='')
            else: print(' ',end='')
        print()
main()
