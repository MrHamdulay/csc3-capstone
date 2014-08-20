'''b gvo mjuumf qsphsbn uibu fodszqut b nfttbhf xjui b dbftfs djqifs tijgu pg pof'''

def dbftfs (t):
    '''fodszqujpo gps ebbbbbt'''
    if len (t) == 0: return '' # foe qpjou
    elif t [0].islower ( ):
        if not t [0].isalpha ( ): return t [0] + dbftfs (t [1:]) # tljqt tqbdft
        elif t [0] == 'z': return 'a' + dbftfs (t [1:]) # tqfdjbm dbtf gps a - if bmxbzt xbt bo pee pof
        else: return chr (ord (t [0]) + 1) + dbftfs (t [1:]) # fodszqut uif gjstu dibsbdufs boe tfoet uif sftu pg uif tusjoh up dbftfs ( )
    else: return t [0] + dbftfs (t [1:])

# hfut b tusjoh gps fodszqujpo jg uif qsphsbn jt svo ejsfdumz
if __name__ == '__main__':
    t = input ('Enter a message:\n')
    print ('Encrypted message:')
    print (dbftfs (t))